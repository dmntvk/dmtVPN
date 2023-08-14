import os
from dotenv import load_dotenv
from pyqiwip2p import QiwiP2P
from yoomoney import Client


load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

YoMoney_Token = str(os.getenv('yoo_token'))


admin_id = [
    331224038
]

ip = os.getenv('ip')
PGUSER = str(os.getenv('PGUSER'))
PGPASS = str(os.getenv('PGPASS'))
DATABASE = str(os.getenv('DATABASE'))

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASS}@{ip}/{DATABASE}'
