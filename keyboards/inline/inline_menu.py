from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import data.config
from utils.dbapi import quick_commands







start_card3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Начать', callback_data='card_start3'),
    ]
])

next_card = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Показать карту настоящего', callback_data='today_card'),
    ]
])

n_card = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Показать карту будущего', callback_data='next_card'),
    ]
])

start_love = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Начать', callback_data='start_love'),
    ]
])

two_cards = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Показать карту представляющая вашего партнера', callback_data='two_cards'),
    ]
])

the_cards = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Показать карту подключения', callback_data='the_cards'),
    ]
])

fo_cards = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Показать карту силы ваших отношений', callback_data='fo_cards'),
    ]
])

fiv_cards = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Показать карту слабых мест ваших отношений', callback_data='fiv_cards'),
    ]
])

six_cards = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Показать вашу настоящую любовную карту', callback_data='six_cards'),
    ]
])

b_up_menu = InlineKeyboardMarkup(inline_keyboard=
                                 [
                                     [
                                    InlineKeyboardButton('79₽', callback_data='79'),
                                     InlineKeyboardButton('170₽', callback_data='170'),
                                     ],
                                        [
                                           InlineKeyboardButton('300₽', callback_data='300'),
                                           InlineKeyboardButton('500₽', callback_data='500'),
                                       ]
                                 ]
)


def oplata(isUrl=True, url='', bill=''):



    qiwiMenu = InlineKeyboardMarkup(row_width=1)
    if isUrl:
        oplata_link = InlineKeyboardButton(text='Оплатить', url=url)
        qiwiMenu.insert(oplata_link)
    btncheckQiwi = InlineKeyboardButton(text='Проверить оплату', callback_data='check_'+bill)
    qiwiMenu.insert(btncheckQiwi)
    cancel = InlineKeyboardButton(text='Отменить оплату', callback_data='cancel'+bill)
    qiwiMenu.insert(cancel)
    return qiwiMenu



sub_menu = InlineKeyboardMarkup(inline_keyboard=
                                [
                                    [
                                        InlineKeyboardButton('Подписаться!', url='https://t.me/tarotvisions')
                                    ],
                                    [
                                        InlineKeyboardButton('Проверить подписку!', callback_data='checks_sub')
                                    ]
                                ])


gotovo_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Outline для Android', url='https://play.google.com/store/apps/details?id=org.outline.android.client'),
        InlineKeyboardButton('Outline для iOS', url='https://apps.apple.com/us/app/outline-app/id1356177741'),
    ],
    [
        InlineKeyboardButton('Outline для Windows', url='https://s3.amazonaws.com/outline-releases/client/windows/stable/Outline-Client.exe'),
        InlineKeyboardButton('Outline для MacOS', url='https://apps.apple.com/us/app/outline-app/id1356178125'),
    ]
])

free_sub = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('🛡️ Получить бесплатную подписку', callback_data='free_subs'),
    ]
])