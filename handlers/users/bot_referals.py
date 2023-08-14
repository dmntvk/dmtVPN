from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import ref_menu
from aiogram.utils.deep_linking import get_start_link


@dp.message_handler(text='🤝 Реферальная программа')
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        ref_link = await get_start_link(payload=message.from_user.id)
        await message.answer(f'<strong>Пригласи в бота 10 друзей и получи на счет 50₽!</strong>\n'
                             f' · Количество рефералов можно посмотреть в разделе "⚙️ Аккаунт"\n'
                             f' · После того как вы пригласили 10 друзей, свяжитесь с тех.поддержкой и они вам начислят ваш бонус.\n'
                             f'\n'
                             f'<strong>Твоя реф. ссылка: </strong>\n'
                             f'<code>{ref_link}</code>', reply_markup=ref_menu)