from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🖥 Подключить VPN'),
            KeyboardButton(text='🆘️ Как пользоваться?'),
        ], [
            KeyboardButton(text='⚙️ Аккаунт'),
        ]
    ], resize_keyboard=True
)

buy_sub = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💳 Купить подписку'),
            KeyboardButton(text='⚙️ Аккаунт'),

        ], [
            KeyboardButton(text='🆘️ Как пользоваться?'),
        ]
    ], resize_keyboard=True
)

profile_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🖥 Подключить VPN'),
            KeyboardButton(text='📥 Пополнить баланс'),
            KeyboardButton(text='💳 Купить подписку'),
        ],
        [
            KeyboardButton(text='💸️ Промокод')
        ],
        [
            KeyboardButton(text='🤝 Реферальная программа')
        ]
    ], resize_keyboard=True
)

ref_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⚙️ Аккаунт')
        ]
    ], resize_keyboard=True
)

faunds_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📥 Пополнить баланс'),
            KeyboardButton(text='⚙️ Аккаунт'),
        ]
    ],     resize_keyboard=True
)


amount_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='60'),
            KeyboardButton(text='110'),
        ],
        [
            KeyboardButton(text='149'),
            KeyboardButton(text='399'),
        ],
        [
            KeyboardButton(text='Отменить оплату ❌'),
        ]
    ],     resize_keyboard=True
)

promo_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔙 Назад'),]
    ], resize_keyboard=True
)

subscribe = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1 день - Бесплатно'),
            KeyboardButton(text='3 дня - 60₽'),
            KeyboardButton(text='7 дней - 110₽'),

        ], [
            KeyboardButton(text='30 дней - 149₽'),
            KeyboardButton(text='90 дней - 399₽'),

        ],
        [KeyboardButton(text='🔙 Назад'),]
    ], resize_keyboard=True
)

help_meny = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🖥 Видеоинструкции'),
            KeyboardButton(text='🆘️ Как пользоваться?'),
        ], [
            KeyboardButton(text='⚙️ Аккаунт'),
        ]
    ], resize_keyboard=True
)