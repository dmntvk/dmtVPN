from aiogram import types
from loader import dp
from keyboards.inline.inline_menu import b_up_menu, oplata
from keyboards.default.keyboard_menu import start_menu, amount_menu
from utils.dbapi import quick_commands
import random
# from data.config import p2p
from states.dep import Dep
from aiogram.dispatcher import FSMContext
from yoomoney import Quickpay
from yoomoney import Client
from data.config import YoMoney_Token

token = YoMoney_Token


@dp.message_handler(text='📥 Пополнить баланс')
async def command_error(message: types.Message):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'Введите сумму пополнения:\n', parse_mode='html', reply_markup=amount_menu)
            await Dep.amount.set()
        if user.status == 'ban':
            await message.answer('Вы заблокированы за махинации')


@dp.message_handler(state=Dep.amount)
async def sum10(message: types.Message, state: FSMContext):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            async with state.proxy() as amount:
                amount['amount'] = message.text
                amounts = amount['amount'].isdigit()
                if amounts == True:
                    if int(amount['amount']) >= 10.0:
                        am = int(amount['amount'])
                        comment = str(message.from_user.id) + '_' + str(random.randint(1000, 9999999))
                        while True:
                            try:
                                await state.finish()
                                quickpay = Quickpay(
                                    receiver="4100118274246347",
                                    quickpay_form="shop",
                                    targets="Sponsor this project",
                                    paymentType="SB",
                                    sum=am,
                                    label=F"{comment}"
                                )
                                await quick_commands.create_check(user_id=message.from_user.id, amount=am, bill_id=quickpay.label,
                                                                  url_p=quickpay.redirected_url)
                                await message.answer('Счет на оплату создан!', reply_markup=start_menu)
                                await message.answer(
                                    f'Вам нужно отправить {am}₽ на наш счет оплатить можно картой(Мир, Visa, MasterCard)\n',
                                    reply_markup=oplata(url=quickpay.redirected_url, bill=quickpay.label))
                                break
                            except:
                                print(f'error dep create - {message.from_user.id}')
                    else:
                        await message.answer(
                            f'Минимальная сумма пополнения 10₽!\n'
                            f'Введите сумму:')
                if amounts == False:
                    if amount['amount'] == 'Отменить оплату ❌':
                        await state.finish()
                        await message.answer('Выберите действие:', reply_markup=start_menu)
                    else:
                        await message.answer(f'Сумму вывода нужно указать цифрами!\n')


# @dp.callback_query_handler(text='10')
# async def sum10(message: types.CallbackQuery):
#     amount = 10
#     await message.message.delete()
#     comment = str(message.from_user.id) + '_' + str(random.randint(1000, 9999999))
#     bill = await p2p.bill(amount=amount, lifetime=15, comment=comment)
#     await quick_commands.create_check(user_id=message.from_user.id, amount=amount, bill_id=bill.bill_id, url_p=bill.pay_url)
#     await message.message.answer(f'Вам нужно отправить {amount}₽ на наш счет Qiwi или оплатить Картой(Мир, Visa, MasterCard)\n', reply_markup=oplata(url=bill.pay_url, bill=bill.bill_id))
#
#
# @dp.callback_query_handler(text='25')
# async def sum10(message: types.CallbackQuery):
#     amount = 25
#     await message.message.delete()
#     comment = str(message.from_user.id) + '_' + str(random.randint(1000, 9999999))
#     bill = p2p.bill(amount=amount, lifetime=15, comment=comment)
#     await quick_commands.create_check(user_id=message.from_user.id, amount=amount, bill_id=bill.bill_id, url_p=bill.pay_url)
#     await message.message.answer(f'Вам нужно отправить {amount}₽ на наш счет Qiwi или оплатить Картой(Мир, Visa, MasterCard)\n', reply_markup=oplata(url=bill.pay_url, bill=bill.bill_id))
#
#
# @dp.callback_query_handler(text='50')
# async def sum10(message: types.CallbackQuery):
#     amount = 50
#     await message.message.delete()
#     comment = str(message.from_user.id) + '_' + str(random.randint(1000, 9999999))
#     bill = p2p.bill(amount=amount, lifetime=15, comment=comment)
#     await quick_commands.create_check(user_id=message.from_user.id, amount=amount, bill_id=bill.bill_id, url_p=bill.pay_url)
#     await message.message.answer(f'Вам нужно отправить {amount}₽ на наш счет Qiwi или оплатить Картой(Мир, Visa, MasterCard)\n', reply_markup=oplata(url=bill.pay_url, bill=bill.bill_id))
#
#
# @dp.callback_query_handler(text='100')
# async def sum10(message: types.CallbackQuery):
#     amount = 100
#     await message.message.delete()
#     comment = str(message.from_user.id) + '_' + str(random.randint(1000, 9999999))
#     bill = p2p.bill(amount=amount, lifetime=15, comment=comment)
#     await quick_commands.create_check(user_id=message.from_user.id, amount=amount, bill_id=bill.bill_id, url_p=bill.pay_url)
#     await message.message.answer(f'Вам нужно отправить {amount}₽ на наш счет Qiwi или оплатить Картой(Мир, Visa, MasterCard)\n', reply_markup=oplata(url=bill.pay_url, bill=bill.bill_id))
#
#
# @dp.callback_query_handler(text='250')
# async def sum10(message: types.CallbackQuery):
#     amount = 250
#     await message.message.delete()
#     comment = str(message.from_user.id) + '_' + str(random.randint(1000, 9999999))
#     bill = p2p.bill(amount=amount, lifetime=15, comment=comment)
#     await quick_commands.create_check(user_id=message.from_user.id, amount=amount, bill_id=bill.bill_id, url_p=bill.pay_url)
#     await message.message.answer(f'Вам нужно отправить {amount}₽ на наш счет Qiwi или оплатить Картой(Мир, Visa, MasterCard)\n', reply_markup=oplata(url=bill.pay_url, bill=bill.bill_id))
#
# @dp.callback_query_handler(text='500')
# async def sum10(message: types.CallbackQuery):
#     amount = 500
#     await message.message.delete()
#     comment = str(message.from_user.id) + '_' + str(random.randint(1000, 9999999))
#     bill = p2p.bill(amount=amount, lifetime=15, comment=comment)
#     await quick_commands.create_check(user_id=message.from_user.id, amount=amount, bill_id=bill.bill_id, url_p=bill.pay_url)
#     await message.message.answer(f'Вам нужно отправить {amount}₽ на наш счет Qiwi или оплатить Картой(Мир, Visa, MasterCard)\n', reply_markup=oplata(url=bill.pay_url, bill=bill.bill_id))


@dp.callback_query_handler(text_contains='check_')
async def check(callback: types.CallbackQuery):
    bill = str(callback.data[6:])
    info = await quick_commands.get_check(bill_id=bill)
    if info != False:
        client = Client(token)
        history = client.operation_history(label=f"{bill}")

        for operation in history.operations:
            if operation.status == 'success':
                await callback.message.delete()
                await quick_commands.deposit_balance(user_id=callback.from_user.id, amount=float(info.amount))
                await callback.message.answer(f'Ваш счет успешно пополнен на {info.amount}₽', reply_markup=start_menu)
                await quick_commands.del_check(bill_id=bill)
        else:
            await callback.message.delete()
            await dp.bot.send_message(callback.from_user.id, 'Вы не оплатили счет!', reply_markup=oplata(url=info.url_p, bill=bill))
    else:
        await dp.bot.send_message(callback.from_user.id, 'Счет не найден')

@dp.callback_query_handler(text_contains='cancel')
async def delceck(callback: types.CallbackQuery):
    bill = str(callback.data[6:])
    await quick_commands.del_check(bill_id=bill)
    await callback.message.delete()
    await callback.message.answer('Счет на оплату удален!', reply_markup=start_menu)