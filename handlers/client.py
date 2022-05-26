from aiogram import types, Dispatcher
# from keyboards import kb

"""Обработчики пользовательских команд"""


async def start(message: types.Message):
    await message.answer('Бот активирован. Чтобы выдать права нужно прописать ваш id в config файл, получить ваш id можно командой /id')


async def get_id(message: types.Message):
    return await message.answer(f'Ваш id: {message.from_user.id}')


async def get_dev(message: types.Message):
    await message.answer(
        """
XV0ST0V_

# Offer Tracker Bot for Telegram

# Telegram: @xvostov_k
# Email: Xvostov.k@yandex.ru

        """)


def register_client_handlers(dp: Dispatcher):
    """Регистрация хендлеров этого файла"""
    dp.register_message_handler(start, commands=['start', 'help'])
    dp.register_message_handler(get_id, commands=['id'])
    dp.register_message_handler(get_dev, commands=['dev'])