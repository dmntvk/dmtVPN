from utils.dbapi.db_gino import TimedBaseModel
from sqlalchemy import Column, BigInteger, String, sql, Float, INTEGER


class User(TimedBaseModel):
    __tablename__ = 'user'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger, primary_key=True)
    f_name = Column(String(200))
    l_name = Column(String(200))
    username = Column(String(50))
    referral_id = Column(BigInteger)
    status = Column(String(30))
    balance = Column(Float)
    subscribe = Column(String(50))
    its_free = Column(INTEGER)

    query: sql.select


class Check(TimedBaseModel):
    __tablename__ = 'check'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    bill_id = Column(String(255))
    user_id = Column(BigInteger)
    amount = Column(BigInteger)
    url_p = Column(String(500))

    query: sql.select


class Promocode(TimedBaseModel):
    __tablename__ = 'promo-code'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    promo = Column(String(50), primary_key=True)
    amount = Column(BigInteger)

    query: sql.select


class Promoactive(TimedBaseModel):
    __tablename__ = 'promo-active'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    promo = Column(String(50))
    user_id = Column(BigInteger)

    query: sql.select


class users_tunel(TimedBaseModel):
    __tablename__ = 'users-tunel'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger)
    country = Column(String(255))
    url = Column(String(500))
    subscribe = Column(String(50))

    query: sql.select