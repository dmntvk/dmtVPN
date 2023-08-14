from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import subscribe, start_menu, faunds_menu, help_meny
from utils.dbapi import quick_commands
import time
import datetime as DT
import random
from datetime import datetime
from outline_vpn.outline_vpn import OutlineVPN


Poland_Server = OutlineVPN(api_url="",
                    cert_sha256="")
USA_Server = OutlineVPN(api_url="",
                    cert_sha256="")

def days_ost(sec):
    seconds = int(sec)
    minute = seconds // 60
    horse = minute // 60
    day = horse // 24
    return day

def names(url):
    url_new = url.partition('ss://')[2]
    url_new = url_new.partition('/?outline=1')[0]
    return url_new


@dp.message_handler(text='💳 Купить подписку')
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            dt = DT.datetime.fromisoformat(f'{datetime.now()}')
            if int(user.subscribe) >= int(dt.timestamp()):
                ostatok = int(user.subscribe) - int(dt.timestamp())
                s = str(time.strftime('%d', time.gmtime(ostatok)))
                if int(s) == 1 or 21:
                    daysz = 'день'
                elif int(s) == 2 or 3 or 4 or 22 or 23 or 24:
                    daysz = 'дня'
                elif int(s) == 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 25 or 26 or 27 or 28 or 29 or 30 or 31:
                    daysz = 'дней'
                await message.answer(f'У вас уже есть подписка! Она закончится через {int(days_ost(ostatok))} {daysz}')
            else:
                await message.answer(f'<strong>Выберите период подписки:</strong>\n'
                                     f'<strong>1 день -</strong> Бесплатно\n'
                                     f'<strong>3 дня -</strong> 60₽\n'
                                     f'<strong>7 дней -</strong> 110₽\n'
                                     f'<strong>30 дней -</strong> 149₽\n'
                                     f'<strong>90 дней -</strong> 399₽\n', parse_mode='html', reply_markup=subscribe)
        if user.status == 'ban':
            await message.answer('Вы заблокированы!')

@dp.message_handler(text='1 день - Бесплатно')
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            if user.its_free == 0:
                await message.answer(f'⏳ Секунду. Активирую бесплатную подписку.', parse_mode='html',
                                     reply_markup=start_menu)
                await quick_commands.subscribe_add(user_id=message.from_user.id, time=86400)
                dt = DT.datetime.fromisoformat(f'{datetime.now()}')
                client = random.SystemRandom().choice([Poland_Server, USA_Server])
                new_key = client.create_key()
                client.rename_key(new_key.key_id, f"{message.from_user.id}")
                await quick_commands.free(user_id=message.from_user.id)
                await quick_commands.create_url(user_id=message.from_user.id, country='PL', url=new_key.access_url, subscribe=f"{int(dt.timestamp()) + 86400}")
                await message.answer(f'<strong>Вы успешно получили пробную подписку на 1 день!</strong>\n'
                                     f'🔑 <strong>Ваш ключ:</strong> (нажми для копирования) <code>ss://{names(new_key.access_url)}#dmtVPN</code>\n', parse_mode='html', reply_markup=help_meny)
                await message.answer(f'<strong>Шаг 1: Скачайте приложение</strong>\n'
                                     f'<a href="https://play.google.com/store/apps/details?id=org.outline.android.client">Android</a> | <a href="https://apps.apple.com/us/app/outline-app/id1356177741">iPhone</a> | <a href="https://s3.amazonaws.com/outline-releases/client/windows/stable/Outline-Client.exe">Windows</a> | <a href="https://apps.apple.com/us/app/outline-app/id1356178125">MacOS</a>\n'
                                     f'\n'
                                     f'<strong>Шаг 2: Скопируйте ключ и вставьте в приложение</strong>\n'
                                     f'\n'
                                     f'<strong>Шаг 3: Подключайтесь!</strong>', parse_mode='html', reply_markup=help_meny, disable_web_page_preview=True)
            if user.its_free == 1:
                await message.answer(f'Вы уже активировали пробную подписку!\n'
                                     f'\n', parse_mode='html', reply_markup=faunds_menu)
        if user.status == 'ban':
            await message.answer('Вы заблокированы!')

@dp.message_handler(text='3 дня - 60₽')
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            if user.balance >= 60.0:
                await message.answer(f'⏳ Секунду. Активирую подписку.', parse_mode='html', reply_markup=start_menu)
                await quick_commands.gdn_balance(user_id=message.from_user.id, amount=60)
                await quick_commands.subscribe_add(user_id=message.from_user.id, time=259200)
                dt = DT.datetime.fromisoformat(f'{datetime.now()}')
                client = random.SystemRandom().choice([Poland_Server, USA_Server])
                new_key =  client.create_key()
                client.rename_key(new_key.key_id, f"{message.from_user.id}")
                await quick_commands.create_url(user_id=message.from_user.id, country='PL', url=new_key.access_url, subscribe=f"{int(dt.timestamp()) + 259200}")
                await message.answer(f'<strong>Вы успешно приобрели подписку на 3 дня!</strong>\n'
                                     f'🔑 <strong>Ваш ключ:</strong> (нажми для копирования) <code>ss://{names(new_key.access_url)}#dmtVPN</code>', parse_mode='html', reply_markup=help_meny)
            elif user.balance <= 59.9:
                await message.answer(f'У Вас не достаточно средств на эту подписку, пополните баланс!\n'
                                             f'\n', parse_mode='html', reply_markup=faunds_menu)
        if user.status == 'ban':
            await message.answer('Вы заблокированы!')

@dp.message_handler(text='7 дней - 110₽')
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            if user.balance >= 110.0:
                await message.answer(f'⏳ Секунду. Активирую подписку.', parse_mode='html', reply_markup=start_menu)
                await quick_commands.gdn_balance(user_id=message.from_user.id, amount=110)
                await quick_commands.subscribe_add(user_id=message.from_user.id, time=604800)
                dt = DT.datetime.fromisoformat(f'{datetime.now()}')
                client = random.SystemRandom().choice([Poland_Server, USA_Server])
                new_key = client.create_key()
                client.rename_key(new_key.key_id, f"{message.from_user.id}")
                await quick_commands.create_url(user_id=message.from_user.id, country='PL', url=new_key.access_url,
                                                subscribe=f"{int(dt.timestamp()) + 604800}")
                await message.answer(f'<strong>Вы успешно приобрели подписку на 7 дней!</strong>\n'
                                     f'🔑 <strong>Ваш ключ:</strong> (нажми для копирования) <code>ss://{names(new_key.access_url)}#dmtVPN</code>',
                                     parse_mode='html', reply_markup=help_meny)
            elif user.balance <= 109.9:
                await message.answer(f'У Вас не достаточно средств на эту подписку, пополните баланс!\n'
                                             f'\n', parse_mode='html', reply_markup=faunds_menu)
        if user.status == 'ban':
            await message.answer('Вы заблокированы!')

@dp.message_handler(text='30 дней - 149₽')
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            if user.balance >= 149.0:
                await message.answer(f'⏳ Секунду. Активирую подписку.', parse_mode='html', reply_markup=start_menu)
                await quick_commands.gdn_balance(user_id=message.from_user.id, amount=149)
                await quick_commands.subscribe_add(user_id=message.from_user.id, time=2592000)
                dt = DT.datetime.fromisoformat(f'{datetime.now()}')
                client = random.SystemRandom().choice([Poland_Server, USA_Server])
                new_key = client.create_key()
                client.rename_key(new_key.key_id, f"{message.from_user.id}")
                await quick_commands.create_url(user_id=message.from_user.id, country='PL', url=new_key.access_url,
                                                subscribe=f"{int(dt.timestamp()) + 2592000}")
                await message.answer(f'<strong>Вы успешно приобрели подписку на 30 дней!</strong>\n'
                                     f'🔑 <strong>Ваш ключ:</strong> (нажми для копирования) <code>ss://{names(new_key.access_url)}#dmtVPN</code>',
                                     parse_mode='html', reply_markup=help_meny)
            elif user.balance <= 148.9:
                await message.answer(f'У Вас не достаточно средств на эту подписку, пополните баланс!\n'
                                             f'\n', parse_mode='html', reply_markup=faunds_menu)
        if user.status == 'ban':
            await message.answer('Вы заблокированы!')

@dp.message_handler(text='90 дней - 399₽')
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            if user.balance >= 399.0:
                await message.answer(f'⏳ Секунду. Активирую подписку.', parse_mode='html', reply_markup=start_menu)
                await quick_commands.gdn_balance(user_id=message.from_user.id, amount=399)
                await quick_commands.subscribe_add(user_id=message.from_user.id, time=7776000)
                dt = DT.datetime.fromisoformat(f'{datetime.now()}')
                client = random.SystemRandom().choice([Poland_Server, USA_Server])
                new_key = client.create_key()
                client.rename_key(new_key.key_id, f"{message.from_user.id}")
                await quick_commands.create_url(user_id=message.from_user.id, country='PL', url=new_key.access_url,
                                                subscribe=f"{int(dt.timestamp()) + 7776000}")
                await message.answer(f'<strong>Вы успешно приобрели подписку на 90 дней!</strong>\n'
                                     f'🔑 <strong>Ваш ключ:</strong> (нажми для копирования) <code>ss://{names(new_key.access_url)}#dmtVPN</code>',
                                     parse_mode='html', reply_markup=help_meny)
            elif user.balance <= 398.9:
                await message.answer(f'У Вас не достаточно средств на эту подписку, пополните баланс!\n'
                                             f'\n', parse_mode='html', reply_markup=faunds_menu)
        if user.status == 'ban':
            await message.answer('Вы заблокированы!')


@dp.callback_query_handler(text='free_subs')
async def command_start(message: types.CallbackQuery):
    if message.message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            if user.its_free == 0:
                await message.message.answer(f'⏳ Секунду. Активирую бесплатную подписку.', parse_mode='html', reply_markup=start_menu)
                await quick_commands.subscribe_add(user_id=message.from_user.id, time=86400)
                dt = DT.datetime.fromisoformat(f'{datetime.now()}')
                client = random.SystemRandom().choice([Poland_Server, USA_Server])
                new_key = client.create_key()
                client.rename_key(new_key.key_id, f"{message.from_user.id}")
                await quick_commands.free(user_id=message.from_user.id)
                await quick_commands.create_url(user_id=message.from_user.id, country='PL', url=new_key.access_url, subscribe=f"{int(dt.timestamp()) + 86400}")
                await message.message.answer(f'<strong>Вы успешно получили пробную подписку на 1 день!</strong>\n'
                                     f'🔑 <strong>Ваш ключ:</strong> (нажми для копирования) <code>ss://{names(new_key.access_url)}#dmtVPN</code>', parse_mode='html', reply_markup=help_meny)
                await message.message.answer(f'<strong>Шаг 1: Скачайте приложение</strong>\n'
                                     f'<a href="https://play.google.com/store/apps/details?id=org.outline.android.client">Android</a> | <a href="https://apps.apple.com/us/app/outline-app/id1356177741">iPhone</a> | <a href="https://s3.amazonaws.com/outline-releases/client/windows/stable/Outline-Client.exe">Windows</a> | <a href="https://apps.apple.com/us/app/outline-app/id1356178125">MacOS</a>\n'
                                     f'\n'
                                     f'<strong>Шаг 2: Скопируйте ключ и вставьте в приложение</strong>\n'
                                     f'\n'
                                     f'<strong>Шаг 3: Подключайтесь!</strong>', parse_mode='html', reply_markup=help_meny, disable_web_page_preview=True)
            if user.its_free == 1:
                await message.message.answer(f'Вы уже активировали пробную подписку!\n'
                                     f'\n', parse_mode='html', reply_markup=faunds_menu)
        if user.status == 'ban':
            await message.answer('Вы заблокированы!')

@dp.message_handler(text='🔙 Назад')
async def back(message: types.Message):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer('Выберите действие:', reply_markup=start_menu)
        if user.status == 'ban':
            await message.answer('Вы заблокированы!')