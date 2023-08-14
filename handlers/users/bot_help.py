from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import start_menu
from keyboards.inline.inline_menu import gotovo_menu
from utils.dbapi import quick_commands


@dp.message_handler(text='🆘️ Как пользоваться?')
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(
                f'1️⃣ Для подключения к VPN необходимо установить приложение Outline. Оно бесплатное и работает во всех популярных операционных системах. Вы можете установить его на свой компьютер, телефон, планшет или на все устройства сразу.\n'
                f'\n'
                f'2️⃣ После оплаты или подключив тестовый период, вы получите ваш уникальный ключ доступа к VPN-серверу такого вида:”ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MT@vpn.server.com” [ ! ] Важно: не публикуйте свой ключ в интернете и не передавайте его третьим лицам. \n'
                f'\n'
                f'3️⃣ Откройте установленное приложение и добавьте в него ключ.  \n'
                f'\n'
                f'Готово! \n',
                parse_mode='html',
                reply_markup=gotovo_menu)
        if user.status == 'ban':
            await message.answer('Вы заблокированы!')


@dp.message_handler(text='🖥 Видеоинструкции')
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.bot.send_video(message.from_user.id, open('/Users/solo/Desktop/dmtVPN/handlers/users/IMG_8350.MP4', 'rb'))
        if user.status == 'ban':
            await message.answer('Вы заблокированы!')
