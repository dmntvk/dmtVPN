from aiogram import Bot, types, Dispatcher
from data import config
from utils.dbapi.db_gino import db
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())


storage = MemoryStorage
__all__ = ['bot', 'dp', 'db']