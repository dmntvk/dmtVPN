from aiogram import types
from loader import dp
from utils.dbapi import quick_commands


@dp.message_handler()
async def command_error(message: types.Message):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'Такой команды нет в моем функционале\n', parse_mode='html')

        if user.status == 'ban':
            await message.answer('Вы заблокированы!')