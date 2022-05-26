from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import MessageTextIsEmpty

from settings import admins_list
from loader import dp
import api


class FSMAddCategory(StatesGroup):
    get_url = State()


class FSMRemoveCategory(StatesGroup):
    get_url = State()


"""Обработчики админских команд"""


# Декоратор для проверки доступа
def check_access(func):
    async def wrapper(*args):
        if admins_list == ['']:
            return await args[0].reply('Администраторы не добавлены', reply=False)
        elif str(args[0].from_user.id) not in admins_list:
            return await args[0].reply('У вас нет доступа для использования команд бота', reply=False)
        else:
            return await func(*args)

    return wrapper


async def cancel_state(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.reply('Процесс завершен')


# Точка входа в машину состояний команды /add_category
@check_access
async def add_category(message: types.Message):
    await FSMAddCategory.get_url.set()
    await message.answer('Отправьте ссылку для добавление в отслеживаемые категории, для отмены отправьте /cancel')


async def add_url_to_categories(message: types.Message, state: FSMContext):

    try:
        api.add_category(message.text)

    except Exception:
        await message.reply('Не удалось добавить адрес в отслеживаемые категории')
    else:
        await message.reply('Адрес успешно добавлен в отслеживаемые категории')

    finally:
        await state.finish()


# Точка входа в машину состояний команды /remove_category
@check_access
async def remove_category(message: types.Message):
    await FSMRemoveCategory.get_url.set()
    await message.answer('Отправьте ссылку для удаления из отслеживаемых категорий, для отмены отправьте /cancel')


async def remove_url_from_categories(message: types.Message, state: FSMContext):
    try:
        api.remove_category(message.text)
    except Exception:
        await message.reply('Не удалось удалить адрес из отслеживаемых')
    else:
        await message.reply('Адрес успешно удален из отслеживаемых категорий')

    finally:
        await state.finish()


@check_access
async def get_categories(message: types.Message):
    try:
        url_list = api.get_categories()

    except Exception:
        await message.answer('Не удалось получить список категорий')
    else:
        try:
            for el in url_list:
                to_send = []
                for i in range(3):
                    if url_list:
                        to_send.append(url_list.pop(0)[0])

                await message.answer(',\n'.join(to_send))
                to_send.clear()

        except MessageTextIsEmpty:
            await message.answer('Cписок пуст')


def register_admins_handlers(dp: Dispatcher):
    """Регистрация хендлеров этого файла"""
    dp.register_message_handler(get_categories, commands=['get_categories'])
    dp.register_message_handler(add_category, commands=['add_category'], state=None)
    dp.register_message_handler(add_url_to_categories, state=FSMAddCategory.get_url)
    dp.register_message_handler(remove_category, commands=['remove_category'], state=None)
    dp.register_message_handler(remove_url_from_categories, state=FSMRemoveCategory.get_url)