import asyncio

from aiogram import executor
from settings import admins_list
# from loader import bot, dp, loop, db
from loader import bot, dp, loop, msg_pool, db_handler
from loguru import logger

from handlers import clients, admins
from aiogram.utils.exceptions import ChatNotFound, ChatIdIsEmpty
import api

chat_id = '767684418'

async def on_startup(_):
    print('Бот запущен')
    try:
        for admin_id in admins_list:
            await bot.send_message(admin_id, 'Бот запущен')
    except ChatNotFound:
        pass
    except ChatIdIsEmpty:
        pass

    return api.listen()


async def msg_handler():
    while True:
        if msg_pool:
            # print(msg_pool)
            offer = msg_pool.pop(0)
            for admin_id in admins_list + db_handler.get_users():
                if offer.img_url:
                    try:
                        await bot.send_photo(admin_id, offer.img_url)
                    except Exception:
                        logger.error(f"Couldn't send photo to {admin_id}")

                try:
                    await bot.send_message(admin_id, f'{offer.title}\n\n{offer.description}\n{offer.price}\n{offer.url}')
                except Exception:
                    logger.error(f"Couldn't send text to {admin_id}")

        await asyncio.sleep(1)

if __name__ == '__main__':
    loop.create_task(msg_handler())
    client.register_client_handlers(dp)
    admins.register_admins_handlers(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
