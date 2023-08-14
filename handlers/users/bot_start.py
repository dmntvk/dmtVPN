from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import start_menu
from keyboards.inline.inline_menu import free_sub
from utils.dbapi import quick_commands
from aiogram.dispatcher.filters import CommandStart
import io




@dp.message_handler(CommandStart())
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        args = message.get_args()
        new_args = await quick_commands.check_args(args, message.from_user.id)
        try:
            user = await quick_commands.select_user(message.from_user.id)
            if user.status == 'active':
                await message.answer(f'<strong>Добро пожаловать в dmtVPN! </strong>👋\n'
                                     f'Я тут, чтобы помочь вам с безопасным и свободным доступом в интернет. 🌐', parse_mode='html', reply_markup=start_menu)
                await message.answer(f'Расскажу немного про наш сервис:\n'
                                     f'🥸 <strong>Простота и удобство </strong>\n'
                                     f'- <code>Пару кликов и ты получишь высокоскоростное и безопасное соединение.</code>\n'
                                     f'\n'
                                     f'🛡️ <strong>Безопасность и анонимность </strong>\n'
                                     f'- <code>Мы не ведем логирования данных наших пользователей, и работаем с эксклюзивными серверами которые обеспечивают безопасность ваших данных.</code>\n'
                                     f'\n'
                                     f'🚀 <strong>Высокая скорость и стабильность</strong>\n'
                                     f'- <code>У нас более 100 серверов по всему миру которые работают 24/7 на высоких скоростях для вашего комфорта.</code>\n'
                                     f'\n'
                                     f'🗺️ <strong>Круглосуточная поддержка</strong>\n'
                                     f'- <code>Наши специалисты находятся онлайн 24/7, чтобы помочь вам если что-то пойдет не так, @dmtVPN_support.</code>\n')
            if user.status == 'ban':
                await message.answer('Вы заблокированы!')
        except Exception:
            await quick_commands.add_user(user_id=message.from_user.id,
                                          f_name=message.from_user.first_name,
                                          l_name=message.from_user.last_name,
                                          referral_id=int(new_args),
                                          username=message.from_user.username,
                                          status='active',
                                          balance=0,
                                          subscribe='0',
                                          its_free=0)
            await message.answer(f'<strong>Добро пожаловать в dmtVPN! </strong>👋\n'
                                 f'\n'
                                 f'Я тут, чтобы помочь вам с безопасным и свободным доступом в интернет. 🌐\n',
                                 parse_mode='html', reply_markup=start_menu)
            await message.answer(f'Расскажу немного про наш сервис:\n'
                                 f'\n'
                                 f'🥸 <strong>Простота и удобство </strong>\n'
                                 f'- <code>Пару кликов и ты получишь высокоскоростное и безопасное соединение.</code>\n'
                                 f'\n'
                                 f'🛡️ <strong>Безопасность и анонимность </strong>\n'
                                 f'- <code>Мы не ведем логирования данных наших пользователей, и работаем с эксклюзивными серверами которые обеспечивают безопасность ваших данных.</code>\n'
                                 f'\n'
                                 f'🚀 <strong>Высокая скорость и стабильность</strong>\n'
                                 f'- <code>У нас более 100 серверов по всему миру которые работают 24/7 на высоких скоростях для вашего комфорта.</code>\n'
                                 f'\n'
                                 f'🗺️ <strong>Круглосуточная поддержка</strong>\n'
                                 f'- <code>Наши специалисты находятся онлайн 24/7, чтобы помочь вам если что-то пойдет не так, @dmtVPN_support.</code>\n')
            await message.answer(f'<strong>Готов попробовать? Подключайся бесплатно!</strong>', reply_markup=free_sub)
