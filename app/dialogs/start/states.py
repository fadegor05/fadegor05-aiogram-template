from aiogram.fsm.state import StatesGroup, State


class StartMenu(StatesGroup):
    first_page = State()
    second_page = State()
