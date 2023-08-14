from utils.dbapi.schemas.user import User, Check, Promocode, Promoactive, users_tunel
from asyncpg import UniqueViolationError
from utils.dbapi.db_gino import db
import random
import datetime as DT
from datetime import datetime
from outline_vpn.outline_vpn import OutlineVPN
from loader import dp
from keyboards.default.keyboard_menu import faunds_menu



# Команды для пользователя
async def add_user(user_id: int, f_name: str, l_name: str, username: str, referral_id: int, status: str,
                   balance: float, subscribe: str, its_free: int):
    try:
        user = User(user_id=user_id, f_name=f_name, l_name=l_name, referral_id=referral_id, username=username,
                    status=status, balance=balance, subscribe=subscribe, its_free=its_free)
        await user.create()
    except UniqueViolationError:
        print('Ошибка добавления юзера')


async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user

async def free(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    free_upd = user.its_free + 1
    await user.update(its_free=free_upd).apply()

async def gdn_balance(user_id: int, amount):
    user = await select_user(user_id)
    new_balance = user.balance - amount
    await user.update(balance=new_balance).apply()


async def user_count():
    users = await User.query.gino.all()
    return len(users)

async def subscribe_add(user_id: int, time):
    dt = DT.datetime.fromisoformat(f'{datetime.now()}')
    user = await select_user(user_id)
    subscribe = int(dt.timestamp()) + time
    await user.update(subscribe=str(subscribe)).apply()

# Рефералы
async def check_args(args, user_id: int):
    if args == '':
        args = '0'
        return args
    elif not args.isnumeric():
        args = '0'
        return args
    elif args.isnumeric():
        if int(args) == user_id:
            args = '0'
            return args
        elif await select_user(user_id=int(args)) is None:
            args = '0'
            return args
        else:
            args = str(args)
            return args
    else:
        args = '0'
        return args


async def count_refs(user_id):
    refs = await User.query.where(User.referral_id == user_id).gino.all()
    return len(refs)


# Работа с балансом и пополнение
async def create_check(user_id: int, amount: int, bill_id: str, url_p: str):
    check = Check(user_id=user_id, amount=amount, bill_id=bill_id, url_p=url_p)
    await check.create()


async def get_check(bill_id: str):
    get_check = await Check.query.where(Check.bill_id == bill_id).gino.first()
    if get_check is None:
        return False
    else:
        return get_check


async def del_check(bill_id: str):
    del_check = await Check.query.where(Check.bill_id == bill_id).gino.first()
    await del_check.delete()


async def deposit_balance(user_id: int, amount):
    user = await select_user(user_id)
    new_balance = user.balance + amount
    await user.update(balance=new_balance).apply()


# Система промокода
async def promo_check(promo: str):
    promo = await Promocode.query.where(Promocode.promo == promo).gino.first()
    if promo is None:
        return False
    else:
        return True


async def promo_chek_active(user_id: int, promo: str):
    promo_active = await Promoactive.query.where(Promoactive.user_id == user_id).gino.all()
    if promo_active is None:
        return True
    else:
        for prom in promo_active:
            if prom.promo == promo:
                return False


# Работа с туннелями
async def create_url(user_id: int, country: str, url: str, subscribe: str):
    urls = users_tunel(user_id=user_id, country=country, url=url, subscribe=subscribe)
    await urls.create()


async def del_tunnel(user_id: str):
    del_tun = await users_tunel.query.where(users_tunel.user_id == user_id).gino.all()
    await del_tun.delete()


async def select_tunnel(user_id):
    tunnel = await users_tunel.query.where(users_tunel.user_id == user_id).gino.all()
    return tunnel

def names(url):
    url_new = url.partition('@')[2]
    url_new = url_new.partition(':')[0]
    return url_new

async def dell_key():
    res = 0
    key = await users_tunel.query.gino.all()
    for x in range(0, len(key)):
        dt = DT.datetime.fromisoformat(f'{datetime.now()}')
        if int(key[x].subscribe) <= int(dt.timestamp()):
            key_d = await users_tunel.query.where(users_tunel.id == key[x].id).gino.first()
            res = res + 1
            ip = names(key[x].url)
            if ip == '89.191.228.149':
                client = OutlineVPN(api_url="",
                                    cert_sha256="")
                for keys in client.get_keys():
                    if str(key[x].user_id) == str(keys.name):
                        client.delete_key(keys.key_id)
                        user = await User.query.where(User.user_id == key[x].user_id).gino.first()
                        await dp.bot.send_message(chat_id=key[x].user_id, text='Ваша подписка закончилась!\n'
                                                                               'Если у вас возникли какие-то вопросы можете обратится в нашу поддержку:\n'
                                                                               '@dmtVPN_support', reply_markup=faunds_menu)
                        await user.update(subscribe=str(0)).apply()
                        await key_d.delete()

            if ip == '194.87.32.35':
                client = OutlineVPN(api_url="",
                    cert_sha256="")
                for keys in client.get_keys():
                    if str(key[x].user_id) == str(keys.name):
                        client.delete_key(keys.key_id)
                        user = await User.query.where(User.user_id == key[x].user_id).gino.first()
                        await user.update(subscribe=str(0)).apply()
                        await dp.bot.send_message(chat_id=key[x].user_id, text='Ваша подписка закончилась!\n'
                                                                               'Если у вас возникли какие-то вопросы можете обратится в нашу поддержку:\n'
                                                                               '@dmtVPN_support', reply_markup=faunds_menu)
                        await key_d.delete()

    return res
