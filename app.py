async def on_startup(dp):
    # import middlewares
    # middlewares.setup(dp)

    from loader import db
    from utils.dbapi.db_gino import on_startup
    print('бд подключилось')
    await on_startup(dp)
    await db.gino.drop_all()
    await db.gino.create_all()
    print('создало')
    # from utils.notifly_admins import on_startup_notify
    # await on_startup_notify(dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    print('бот начал работу')


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
