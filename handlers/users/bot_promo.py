from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import promo_menu, start_menu
from utils.dbapi import quick_commands
from states.promo_state import Promo
from aiogram.dispatcher import FSMContext


@dp.message_handler(text='💸️ Промокод')
async def command_start(message: types.Message):
    user = await quick_commands.select_user(message.from_user.id)
    if user.status == 'active':
        await Promo.promo_state.set()
        await message.answer(f'Введите промокод:\n'
                             f'\n', parse_mode='html', reply_markup=promo_menu)
    if user.status == 'ban':
        await message.answer('Вы заблокированы за махинации')


@dp.message_handler(state=Promo.promo_state)
async def promo(message: types.Message, state: FSMContext):
    async with state.proxy() as promo:
        promo['promo_state'] = message.text
        if promo['promo_state'] == '🔙 Назад':
            await message.answer('Выберите действие:', reply_markup=start_menu)
            await state.finish()
        else:
            promo_check = await quick_commands.promo_check(promo=promo['promo_state'])
            if promo_check == False:
                await message.answer(f'Промокод введен не верно или его не существует!\n'
                                     f'Проверьте правильность введенного промокода!')
            if promo_check == True:
                active_check = await quick_commands.promo_chek_active(user_id=message.from_user.id, promo=message.text)
                if active_check == False:
                    await message.answer(f'Вы уже активировали данный промокод!\n'
                                         f'Не жульничай 😉', reply_markup=start_menu)
                    await state.finish()
                else:
                    promo_amount = await quick_commands.promo_active(user_id=message.from_user.id, promo=message.text)
                    await message.answer(f'Промокод успешно активирован!\n'
                                         f'На ваш баланс зачислено {promo_amount}', reply_markup=start_menu)
                    await state.finish()

