from aiogram.dispatcher.filters.state import StatesGroup, State

class Dep(StatesGroup):
    amount = State()
