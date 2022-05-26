import asyncio
from flask import Flask
from aiogram import Bot, Dispatcher
from settings import bot_token
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from db import DataBaseHandler
import configparser

msg_pool = []


# is_available = True
# db = DataBaseHandler()
storage = MemoryStorage()
bot = Bot(token=bot_token)
loop = asyncio.get_event_loop()
app = Flask(__name__)
dp = Dispatcher(bot, storage=storage, loop=loop)