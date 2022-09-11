from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import MessageTextIsEmpty

from settings import admins_list
from loader import dp
from loader import db_handler
from loguru import logger
import asyncio
import requests


class FSMAddCategoryAvito1(StatesGroup):
    get_url = State()


class FSMRemoveCategoryAvito1(StatesGroup):
    get_url = State()


class FSMAddCategoryAvito2(StatesGroup):
    get_url = State()


class FSMRemoveCategoryAvito2(StatesGroup):
    get_url = State()


class FSMAddToBlackList(StatesGroup):
    get_id = State()


class FSMRemoveFromBlackList(StatesGroup):
    get_id = State()


class FSMAddStopWord(StatesGroup):
    word = State()


class FSMRemoveStopWord(StatesGroup):
    word = State()


class FSMAddUser(StatesGroup):
    get_chat_id = State()


class FSMRemoveUser(StatesGroup):
    get_chat_id = State()


class FSMAddCategoryOlx1(StatesGroup):
    get_url = State()


class FSMRemoveCategoryOlx1(StatesGroup):
    get_url = State()


class FSMAddCategoryWatch(StatesGroup):
    get_url = State()


class FSMRemoveCategoryWatch(StatesGroup):
    get_url = State()


class FSMAddToBlackListOlx(StatesGroup):
    get_id = State()


class FSMRemoveFromBlackListOlx(StatesGroup):
    get_id = State()


class FSMAddStopwordOlx(StatesGroup):
    word = State()


class FSMRemoveStopwordOlx(StatesGroup):
    word = State()


class FSMAddCategoryLalafo(StatesGroup):
    get_url = State()


class FSMRemoveCategoryLalafo(StatesGroup):
    get_url = State()


class FSMAddStopWordLalafo(StatesGroup):
    word = State()


class FSMRemoveStopWordLalafo(StatesGroup):
    word = State()

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
async def add_category_avito_1(message: types.Message):
    await FSMAddCategoryAvito1.get_url.set()
    await message.answer('Отправьте ссылку для добавление в отслеживаемые категории, для отмены отправьте /cancel')


async def add_url_to_categories_avito_1(message: types.Message, state: FSMContext):
    try:
        db_handler.add_category_to_avito_1(message.text)

    except Exception:
        await message.reply('Не удалось добавить адрес в отслеживаемые категории')
    else:
        await message.reply('Адрес успешно добавлен в отслеживаемые категории')

    finally:
        await state.finish()


# Точка входа в машину состояний команды /add_category
@check_access
async def add_category_avito_2(message: types.Message):
    await FSMAddCategoryAvito2.get_url.set()
    await message.answer('Отправьте ссылку для добавление в отслеживаемые категории, для отмены отправьте /cancel')


async def add_url_to_categories_avito_2(message: types.Message, state: FSMContext):
    try:
        db_handler.add_category_to_avito_2(message.text)

    except Exception:
        await message.reply('Не удалось добавить адрес в отслеживаемые категории')
    else:
        await message.reply('Адрес успешно добавлен в отслеживаемые категории')

    finally:
        await state.finish()


# Точка входа в машину состояний команды /remove_category
@check_access
async def remove_category_avito_1(message: types.Message):
    await FSMRemoveCategoryAvito1.get_url.set()
    await message.answer('Отправьте ссылку для удаления из отслеживаемых категорий, для отмены отправьте /cancel')


async def remove_url_from_categories_avito_1(message: types.Message, state: FSMContext):
    try:
        db_handler.remove_category_from_avito_1(message.text)
    except Exception:
        await message.reply('Не удалось удалить адрес из отслеживаемых')
    else:
        await message.reply('Адрес успешно удален из отслеживаемых категорий')

    finally:
        await state.finish()


# Точка входа в машину состояний команды /remove_category
@check_access
async def remove_category_avito_2(message: types.Message):
    await FSMRemoveCategoryAvito2.get_url.set()
    await message.answer('Отправьте ссылку для удаления из отслеживаемых категорий, для отмены отправьте /cancel')


async def remove_url_from_categories_avito_2(message: types.Message, state: FSMContext):
    try:
        db_handler.remove_category_from_avito_2(message.text)
    except Exception:
        await message.reply('Не удалось удалить адрес из отслеживаемых')
    else:
        await message.reply('Адрес успешно удален из отслеживаемых категорий')

    finally:
        await state.finish()


@check_access
async def get_categories_avito_1(message: types.Message):
    try:
        url_list = db_handler.get_categories_from_avito_1()

    except Exception:
        await message.answer('Не удалось получить список категорий')
    else:
        if url_list:
            while True:
                if url_list:
                    to_send = []
                    for i in range(3):
                        if url_list:
                            to_send.append(url_list.pop(0)[0])

                    await message.answer(',\n'.join(to_send))
                    await asyncio.sleep(0.5)

                else:
                    break
        else:
            await message.answer('Cписок пуст')


@check_access
async def get_categories_avito_2(message: types.Message):
    try:
        url_list = db_handler.get_categories_from_avito_2()

    except Exception:
        await message.answer('Не удалось получить список категорий')
    else:
        if url_list:
            for el in url_list:
                to_send = []
                for i in range(3):
                    if url_list:
                        to_send.append(url_list.pop(0)[0])

                await message.answer(',\n'.join(to_send))
                to_send.clear()

        else:
            await message.answer('Cписок пуст')


# Точка входа в машину состояний команды /add_to_blacklist
@check_access
async def add_to_blacklist(message: types.Message):
    await FSMAddToBlackList.get_id.set()
    await message.answer('Отправьте id продавца для добавление в черный список, для отмены отправьте /cancel')


async def add_url_to_blacklist(message: types.Message, state: FSMContext):
    db_handler.add_to_blacklist(message.text.strip())
    await message.reply('Продавец успешно добавлен в черный список')
    await state.finish()


# Точка входа в машину состояний команды /remove_from_blacklist
@check_access
async def remove_from_blacklist(message: types.Message):
    await FSMRemoveFromBlackList.get_id.set()
    await message.answer('Отправьте id продавца для удаления из черного списка, для отмены отправьте /cancel')


async def remove_url_from_blacklist(message: types.Message, state: FSMContext):
    db_handler.remove_from_blacklist(message.text.strip())
    await message.reply('Продавец успешно удален из черного списка')
    await state.finish()


@check_access
async def get_blacklist(message: types.Message):
    url_list = db_handler.get_blacklist()
    print(db_handler.get_blacklist())
    try:
        await message.answer(',\n'.join(url_list))
    except MessageTextIsEmpty:
        await message.answer('Черный список пуст')


# Точка входа в машину состояний команды /add_stopword
@check_access
async def add_stopword(message: types.Message):
    await FSMAddStopWord.word.set()
    await message.answer('Отправьте стоп слово для сохранения, для отмены отправьте /cancel')


async def push_stopword(message: types.Message, state: FSMContext):
    db_handler.add_stopword(message.text)
    await message.reply('Стоп слово успешно добавлено')
    await state.finish()


# Точка входа в машину состояний команды /remove_stopword
@check_access
async def remove_stopword(message: types.Message):
    await FSMRemoveStopWord.word.set()
    await message.answer('Отправьте стоп слово для его удаления, для отмены отправьте /cancel')


async def throw_out_stopword(message: types.Message, state: FSMContext):
    db_handler.remove_stopword(message.text)
    await message.reply('Стоп слово успешно удалено')
    await state.finish()


@check_access
async def get_stopwords(message: types.Message):
    words = db_handler.get_stopwords()

    try:
        await message.answer(',\n'.join(words))
    except MessageTextIsEmpty:
        await message.answer('Стоп слова отсутствуют')


# ===============================Юзеры==========================================
# Точка входа в машину состояний команды /add_user
@check_access
async def add_user(message: types.Message):
    await FSMAddUser.get_chat_id.set()
    await message.answer('Отправьте чат id для добавления нового пользователя, для отмены отправьте /cancel')


async def add_user_to_db(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        db_handler.add_user(message.text)
        await message.reply('Пользователь успешно добавлен')

    else:
        await message.reply('Введен некорректный чат id')

    await state.finish()


# Точка входа в машину состояний команды /remove_user
@check_access
async def remove_user(message: types.Message):
    await FSMRemoveUser.get_chat_id.set()
    await message.answer('Отправьте чат id для удаления пользователя, для отмены отправьте /cancel')


async def remove_user_from_db(message: types.Message, state: FSMContext):
    db_handler.remove_user(message.text)
    await message.reply('Пользователь успешно удален')
    await state.finish()


@check_access
async def get_users(message: types.Message):
    user_list = db_handler.get_users()

    try:
        await message.answer(',\n'.join([el for el in user_list]))
    except MessageTextIsEmpty:
        await message.answer('Cписок пуст')


# Точка входа в машину состояний команды /add_category_olx_1
@check_access
async def add_category_olx(message: types.Message):
    await FSMAddCategoryOlx1.get_url.set()
    await message.answer('Отправьте ссылку для добавление в отслеживаемые категории, для отмены отправьте /cancel')


async def add_url_to_categories_olx(message: types.Message, state: FSMContext):
    try:
        json = {
            "token": "8Z2g5cktbfIxcUrrcruaaZHnSigabnEU2DZ0ykIYa3LkYoppEe",
            "cmd": "add",
            "url": message.text
        }
        resp = requests.post('http://45.147.200.229:8080/categories', json=json)
        resp.raise_for_status()

    except Exception:
        await message.reply('Не удалось добавить адрес в отслеживаемые категории')
    else:
        await message.reply('Адрес успешно добавлен в отслеживаемые категории')

    finally:
        await state.finish()


@check_access
async def remove_category_olx(message: types.Message):
    await FSMRemoveCategoryOlx1.get_url.set()
    await message.answer('Отправьте ссылку для удаления из отслеживаемых категорий, для отмены отправьте /cancel')


async def remove_url_from_categories_olx(message: types.Message, state: FSMContext):
    try:
        json = {
            "token": "8Z2g5cktbfIxcUrrcruaaZHnSigabnEU2DZ0ykIYa3LkYoppEe",
            "cmd": "remove",
            "url": message.text
        }
        resp = requests.post('http://45.147.200.229:8080/categories', json=json)
        resp.raise_for_status()

    except Exception:
        await message.reply('Не удалось удалить адрес из отслеживаемых')
    else:
        await message.reply('Адрес успешно удален из отслеживаемых категорий')

    finally:
        await state.finish()


@check_access
async def get_categories_olx(message: types.Message):
    try:
        json = {
            "token": "8Z2g5cktbfIxcUrrcruaaZHnSigabnEU2DZ0ykIYa3LkYoppEe",
        }
        resp = requests.get('http://45.147.200.229:8080/categories', json=json)
        resp.raise_for_status()
        url_list = dict(resp.json())
        url_list = url_list.get('categories', '')

    except Exception:
        await message.answer('Не удалось получить список категорий')
    else:
        if url_list:
            while True:
                if url_list:
                    to_send = []
                    for i in range(3):
                        if url_list:
                            to_send.append(url_list.pop(0))

                    await message.answer(',\n'.join(to_send))
                    await asyncio.sleep(0.5)

                else:
                    break
        else:
            await message.answer('Cписок пуст')


# ===============================================================

# Точка входа в машину состояний команды /add_category_watch
@check_access
async def add_category_watch(message: types.Message):
    await FSMAddCategoryWatch.get_url.set()
    await message.answer('Отправьте ссылку для добавление в отслеживаемые категории, для отмены отправьте /cancel')


async def add_url_to_categories_watch(message: types.Message, state: FSMContext):
    try:
        db_handler.add_category_to_watch(message.text)

    except Exception:
        await message.reply('Не удалось добавить адрес в отслеживаемые категории')
    else:
        await message.reply('Адрес успешно добавлен в отслеживаемые категории')

    finally:
        await state.finish()


# Точка входа в машину состояний команды /remove_category_watch
@check_access
async def remove_category_watch(message: types.Message):
    await FSMRemoveCategoryWatch.get_url.set()
    await message.answer('Отправьте ссылку для удаления из отслеживаемых категорий, для отмены отправьте /cancel')


async def remove_url_from_categories_watch(message: types.Message, state: FSMContext):
    try:
        db_handler.remove_category_from_watch(message.text)
    except Exception:
        await message.reply('Не удалось удалить адрес из отслеживаемых')
    else:
        await message.reply('Адрес успешно удален из отслеживаемых категорий')

    finally:
        await state.finish()


@check_access
async def get_categories_watch(message: types.Message):
    try:
        url_list = db_handler.get_categories_from_watch()

    except Exception:
        await message.answer('Не удалось получить список категорий')
    else:
        if url_list:
            for el in url_list:
                to_send = []
                for i in range(3):
                    if url_list:
                        to_send.append(url_list.pop(0)[0])

                await message.answer(',\n'.join(to_send))
                to_send.clear()

        else:
            await message.answer('Cписок пуст')


# Точка входа в машину состояний команды /add_to_blacklist_olx
@check_access
async def add_to_blacklist_olx(message: types.Message):
    await FSMAddToBlackListOlx.get_id.set()
    await message.answer('Отправьте id продавца для добавление в черный список, для отмены отправьте /cancel')


async def push_to_blacklist_olx(message: types.Message, state: FSMContext):
    try:
        json = {
            "token": "8Z2g5cktbfIxcUrrcruaaZHnSigabnEU2DZ0ykIYa3LkYoppEe",
            "cmd": "add",
            "user_id": message.text
        }
        resp = requests.post('http://45.147.200.229:8080/blacklist', json=json)
        resp.raise_for_status()

    except Exception:
        await message.reply('Не удалось добавить id в черный список')
    else:
        await message.reply('Продавец успешно добавлен в черный список')

    finally:
        await state.finish()


# Точка входа в машину состояний команды /remove_from_blacklist
@check_access
async def remove_from_blacklist_olx(message: types.Message):
    await FSMRemoveFromBlackListOlx.get_id.set()
    await message.answer('Отправьте id продавца для удаления из черного списка, для отмены отправьте /cancel')


async def remove_id_from_blacklist_olx(message: types.Message, state: FSMContext):
    try:
        json = {
            "token": "8Z2g5cktbfIxcUrrcruaaZHnSigabnEU2DZ0ykIYa3LkYoppEe",
            "cmd": "remove",
            "user_id": message.text
        }
        resp = requests.post('http://45.147.200.229:8080/blacklist', json=json)
        resp.raise_for_status()

    except Exception:
        await message.reply('Не удалось удалить id из черного списка')
    else:
        await message.reply('Продавец успешно удален из черного списка')

    finally:
        await state.finish()


@check_access
async def get_blacklist_olx(message: types.Message):
    try:
        json = {
            "token": "8Z2g5cktbfIxcUrrcruaaZHnSigabnEU2DZ0ykIYa3LkYoppEe",
        }
        resp = requests.get('http://45.147.200.229:8080/blacklist', json=json)
        resp.raise_for_status()
        blacklist = dict(resp.json())
        blacklist = blacklist.get('ids', '')

    except Exception:
        await message.answer('Не удалось получить список категорий')
    else:
        try:
            await message.answer(',\n'.join(blacklist))
        except MessageTextIsEmpty:
            await message.answer('Черный список пуст')


# ================
# Точка входа в машину состояний команды /add_stopword_olx
@check_access
async def add_stopword_olx(message: types.Message):
    await FSMAddStopwordOlx.word.set()
    await message.answer('Отправьте стоп слово для добавления, для отмены отправьте /cancel')


async def push_stopword_olx(message: types.Message, state: FSMContext):
    try:
        json = {
            "token": "8Z2g5cktbfIxcUrrcruaaZHnSigabnEU2DZ0ykIYa3LkYoppEe",
            "cmd": "add",
            "word": message.text
        }
        resp = requests.post('http://45.147.200.229:8080/stopwords', json=json)
        resp.raise_for_status()

    except Exception:
        await message.reply('Не удалось добавить стоп слово')
    else:
        await message.reply('Стоп слово успешно добавлено')

    finally:
        await state.finish()


# Точка входа в машину состояний команды /remove_from_blacklist
@check_access
async def remove_stopword_olx(message: types.Message):
    await FSMRemoveStopwordOlx.word.set()
    await message.answer('Отправьте стоп слово для удаления, для отмены отправьте /cancel')


async def remove_stopword_from_olx(message: types.Message, state: FSMContext):
    try:
        json = {
            "token": "8Z2g5cktbfIxcUrrcruaaZHnSigabnEU2DZ0ykIYa3LkYoppEe",
            "cmd": "remove",
            "word": message.text
        }
        resp = requests.post('http://45.147.200.229:8080/stopwords', json=json)
        resp.raise_for_status()

    except Exception:
        await message.reply('Не удалось удалить стоп слово')
    else:
        await message.reply('Стоп слово успешно удалено')

    finally:
        await state.finish()


@check_access
async def get_stopwords_olx(message: types.Message):
    try:
        json = {
            "token": "8Z2g5cktbfIxcUrrcruaaZHnSigabnEU2DZ0ykIYa3LkYoppEe",
        }
        resp = requests.get('http://45.147.200.229:8080/stopwords', json=json)
        resp.raise_for_status()
        words = dict(resp.json())
        words = words.get('words', '')

    except Exception:
        await message.answer('Не удалось получить список стоп слов')
    else:
        try:
            await message.answer(',\n'.join(words))
        except MessageTextIsEmpty:
            await message.answer('Список стоп слов пуст')


# =============================

# Точка входа в машину состояний команды /add_category_lalafo
@check_access
async def add_category_lalafo(message: types.Message):
    await FSMAddCategoryLalafo.get_url.set()
    await message.answer('Отправьте ссылку для добавление в отслеживаемые категории, для отмены отправьте /cancel')


async def add_url_to_categories_lalafo(message: types.Message, state: FSMContext):
    try:
        db_handler.add_category_to_lalafo(message.text)

    except Exception:
        await message.reply('Не удалось добавить адрес в отслеживаемые категории')
    else:
        await message.reply('Адрес успешно добавлен в отслеживаемые категории')

    finally:
        await state.finish()


# Точка входа в машину состояний команды /remove_category_lalafo
@check_access
async def remove_category_lalafo(message: types.Message):
    await FSMRemoveCategoryLalafo.get_url.set()
    await message.answer('Отправьте ссылку для удаления из отслеживаемых категорий, для отмены отправьте /cancel')


async def remove_url_from_categories_lalafo(message: types.Message, state: FSMContext):
    try:
        db_handler.remove_category_from_lalafo(message.text)
    except Exception:
        await message.reply('Не удалось удалить адрес из отслеживаемых')
    else:
        await message.reply('Адрес успешно удален из отслеживаемых категорий')

    finally:
        await state.finish()


@check_access
async def get_categories_lalafo(message: types.Message):
    try:
        url_list = db_handler.get_categories_from_lalafo()

    except Exception:
        await message.answer('Не удалось получить список категорий')
    else:
        if url_list:
            for el in url_list:
                to_send = []
                for i in range(3):
                    if url_list:
                        to_send.append(url_list.pop(0)[0])

                await message.answer(',\n'.join(to_send))
                to_send.clear()

        else:
            await message.answer('Cписок пуст')

# ===============================

# Точка входа в машину состояний команды /add_stopword_lalafo
@check_access
async def add_stopword_lalafo(message: types.Message):
    await FSMAddStopWordLalafo.word.set()
    await message.answer('Отправьте стоп слово для сохранения, для отмены отправьте /cancel')


async def push_stopword_lalafo(message: types.Message, state: FSMContext):
    db_handler.add_stopword_lalafo(message.text)
    await message.reply('Стоп слово успешно добавлено')
    await state.finish()


# Точка входа в машину состояний команды /remove_stopword
@check_access
async def remove_stopword_lalafo(message: types.Message):
    await FSMRemoveStopWordLalafo.word.set()
    await message.answer('Отправьте стоп слово для его удаления, для отмены отправьте /cancel')


async def throw_out_stopword_lalafo(message: types.Message, state: FSMContext):
    db_handler.remove_stopword_lalafo(message.text)
    await message.reply('Стоп слово успешно удалено')
    await state.finish()


@check_access
async def get_stopwords_lalafo(message: types.Message):
    words = db_handler.get_stopwords_lalafo()

    try:
        await message.answer(',\n'.join(words))
    except MessageTextIsEmpty:
        await message.answer('Стоп слова отсутствуют')

def register_admins_handlers(dp: Dispatcher):
    """Регистрация хендлеров этого файла"""
    dp.register_message_handler(cancel_state, commands=['cancel'], state='*')
    dp.register_message_handler(get_categories_avito_1, commands=['get_categories_avito_1'])
    dp.register_message_handler(add_category_avito_1, commands=['add_category_avito_1'], state=None)
    dp.register_message_handler(add_url_to_categories_avito_1, state=FSMAddCategoryAvito1.get_url)
    dp.register_message_handler(remove_category_avito_1, commands=['remove_category_avito_1'], state=None)
    dp.register_message_handler(remove_url_from_categories_avito_1, state=FSMRemoveCategoryAvito1.get_url)

    dp.register_message_handler(get_categories_avito_2, commands=['get_categories_avito_2'])
    dp.register_message_handler(add_category_avito_2, commands=['add_category_avito_2'], state=None)
    dp.register_message_handler(add_url_to_categories_avito_2, state=FSMAddCategoryAvito2.get_url)
    dp.register_message_handler(remove_category_avito_2, commands=['remove_category_avito_2'], state=None)
    dp.register_message_handler(remove_url_from_categories_avito_2, state=FSMRemoveCategoryAvito2.get_url)

    dp.register_message_handler(get_blacklist, commands=['get_blacklist'])
    dp.register_message_handler(add_to_blacklist, commands=['add_to_blacklist'], state=None)
    dp.register_message_handler(add_url_to_blacklist, state=FSMAddToBlackList.get_id)
    dp.register_message_handler(remove_from_blacklist, commands=['remove_from_blacklist'], state=None)
    dp.register_message_handler(remove_url_from_blacklist, state=FSMRemoveFromBlackList.get_id)

    dp.register_message_handler(add_stopword, commands=['add_stopword'], state=None)
    dp.register_message_handler(push_stopword, state=FSMAddStopWord.word)
    dp.register_message_handler(get_stopwords, commands=['get_stopwords'])
    dp.register_message_handler(remove_stopword, commands=['remove_stopword'], state=None)
    dp.register_message_handler(throw_out_stopword, state=FSMRemoveStopWord.word)

    dp.register_message_handler(get_users, commands=['get_users'])
    dp.register_message_handler(add_user, commands=['add_user'], state=None)
    dp.register_message_handler(add_user_to_db, state=FSMAddUser.get_chat_id)
    dp.register_message_handler(remove_user, commands=['remove_user'], state=None)
    dp.register_message_handler(remove_user_from_db, state=FSMRemoveUser.get_chat_id)

    dp.register_message_handler(add_category_olx, commands=['add_category_olx'], state=None)
    dp.register_message_handler(add_url_to_categories_olx, state=FSMAddCategoryOlx1.get_url)
    dp.register_message_handler(remove_category_olx, commands=['remove_category_olx'], state=None)
    dp.register_message_handler(remove_url_from_categories_olx, state=FSMRemoveCategoryOlx1.get_url)
    dp.register_message_handler(get_categories_olx, commands=['get_categories_olx'])

    dp.register_message_handler(add_category_watch, commands=['add_category_watch'], state=None)
    dp.register_message_handler(add_url_to_categories_watch, state=FSMAddCategoryWatch.get_url)
    dp.register_message_handler(remove_category_watch, commands=['remove_category_watch'], state=None)
    dp.register_message_handler(remove_url_from_categories_watch, state=FSMRemoveCategoryWatch.get_url)
    dp.register_message_handler(get_categories_watch, commands=['get_categories_watch'])

    dp.register_message_handler(get_blacklist_olx, commands=['get_blacklist_olx'])
    dp.register_message_handler(add_to_blacklist_olx, commands=['add_to_blacklist_olx'], state=None)
    dp.register_message_handler(push_to_blacklist_olx, state=FSMAddToBlackListOlx.get_id)
    dp.register_message_handler(remove_from_blacklist_olx, commands=['remove_from_blacklist_olx'], state=None)
    dp.register_message_handler(remove_id_from_blacklist_olx, state=FSMRemoveFromBlackListOlx.get_id)

    dp.register_message_handler(add_stopword_olx, commands=['add_stopword_olx'], state=None)
    dp.register_message_handler(push_stopword_olx, state=FSMAddStopwordOlx.word)
    dp.register_message_handler(get_stopwords_olx, commands=['get_stopwords_olx'])
    dp.register_message_handler(remove_stopword_olx, commands=['remove_stopword_olx'], state=None)
    dp.register_message_handler(remove_stopword_from_olx, state=FSMRemoveStopwordOlx.word)

    dp.register_message_handler(add_category_lalafo, commands=['add_category_lalafo'], state=None)
    dp.register_message_handler(add_url_to_categories_lalafo, state=FSMAddCategoryLalafo.get_url)
    dp.register_message_handler(remove_category_lalafo, commands=['remove_category_lalafo'], state=None)
    dp.register_message_handler(remove_url_from_categories_lalafo, state=FSMRemoveCategoryLalafo.get_url)
    dp.register_message_handler(get_categories_lalafo, commands=['get_categories_lalafo'])

    dp.register_message_handler(add_stopword_lalafo, commands=['add_stopword_lalafo'], state=None)
    dp.register_message_handler(push_stopword_lalafo, state=FSMAddStopWordLalafo.word)
    dp.register_message_handler(get_stopwords_lalafo, commands=['get_stopwords_lalafo'])
    dp.register_message_handler(remove_stopword_lalafo, commands=['remove_stopword_lalafo'], state=None)
    dp.register_message_handler(throw_out_stopword_lalafo, state=FSMRemoveStopWordLalafo.word)