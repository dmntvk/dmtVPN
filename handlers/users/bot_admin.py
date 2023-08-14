from aiogram import types
from loader import dp
from utils.dbapi import quick_commands

@dp.message_handler(text='юзер')
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 331224038:
            users = await quick_commands.user_count()
            await message.answer(f'Пользователей в боте {users}')
        else:
            await message.answer(f'Такой команды нет в моем функционале\n', parse_mode='html')


@dp.message_handler(text='чистка')
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 331224038:
            users = await quick_commands.dell_key()
            await message.answer(f'Удалил истекших подписок {users}')
        else:
            await message.answer(f'Такой команды нет в моем функционале\n', parse_mode='html')