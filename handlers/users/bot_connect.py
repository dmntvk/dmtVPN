from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import buy_sub, start_menu, help_meny
from utils.dbapi import quick_commands
import time
import datetime as DT
from datetime import datetime

def names(url):
    url_new = url.partition('ss://')[2]
    url_new = url_new.partition('/?outline=1')[0]
    return url_new

@dp.message_handler(text='🖥 Подключить VPN')
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        tunnel = await quick_commands.select_tunnel(message.from_user.id)
        if user.status == 'active':
            dt = DT.datetime.fromisoformat(f'{datetime.now()}')
            if int(user.subscribe) >= int(dt.timestamp()):
                for x in range(0, len(tunnel)):
                    await message.answer(f'<strong>Ваш ключ:</strong>\n'
                                         f'<code>ss://{names(tunnel[x].url)}#dmtVPN</code> (📝 нажмите на текст и ключ скопируется автоматически)', parse_mode='html', reply_markup=help_meny)
            else:
                await message.answer(f'<strong>У вас нет активной подписки!</strong>\n', parse_mode='html', reply_markup=buy_sub)
        if user.status == 'ban':
            await message.answer('Вы заблокированы!')
