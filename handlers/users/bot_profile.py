from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import profile_menu
from utils.dbapi import quick_commands
import time
import datetime as DT
from datetime import datetime

def days_ost(sec):
    seconds = int(sec)
    minute = seconds // 60
    horse = minute // 60
    day = horse // 24
    return day

@dp.message_handler(text='⚙️ Аккаунт')
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        count_ref = await quick_commands.count_refs(message.from_user.id)
        if user.status == 'active':
            create = f'{user.created_at}'
            lst = create.split()
            if user.subscribe == '0':
                await message.answer(f'<strong>Ваш профиль</strong>\n'
                                     f'<em>Вся необходимая информация о вашем профиле</em>\n'
                                     f'\n'
                                     f'👤 <strong>ID: </strong>{user.user_id}\n'
                                     f'💶 <strong>Баланс: {user.balance}</strong>\n'
                                     f'👤 <strong>У вас нет активной подписки!</strong>\n'
                                     f'👨‍👦‍👦 <strong>Рефералы: </strong>{count_ref}\n', parse_mode='html',
                                     reply_markup=profile_menu)
            else:
                dt = DT.datetime.fromisoformat(f'{datetime.now()}')
                ostatok = int(user.subscribe) - int(dt.timestamp())
                s = str(time.strftime('%d', time.gmtime(ostatok)))
                if int(s) == 1 or 21:
                    daysz = 'день'
                elif int(s) == 2 or 3 or 4 or 22 or 23 or 24:
                    daysz = 'дня'
                elif int(s) == 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 25 or 26 or 27 or 28 or 29 or 30 or 31:
                    daysz = 'дней'
                await message.answer(f'<strong>Ваш профиль</strong>\n'
                                     f'<em>Вся необходимая информация о вашем профиле</em>\n'
                                     f'\n'
                                     f'👤 <strong>ID: </strong>{user.user_id}\n'
                                     f'💶 <strong>Баланс: {user.balance}</strong>\n'
                                     f'👤 <strong>Подписка истекает через: </strong>{int(days_ost(ostatok))} {daysz}\n'
                                     f'👨‍👦‍👦 <strong>Рефералы: </strong>{count_ref}\n', parse_mode='html',
                                     reply_markup=profile_menu)
        if user.status == 'ban':
            await message.answer('Вы заблокированы!')
