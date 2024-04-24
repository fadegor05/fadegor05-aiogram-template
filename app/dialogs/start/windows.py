from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Next, Cancel, Back, Button
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.start import states, callbacks, getters


def first_window():
    return Window(
        Format('Hello, it is first page!\nAlso your telegram id is {telegram_id}'),
        Next(Const('Next')),
        Cancel(Const('Cancel')),
        state=states.StartMenu.first_page,
        getter=getters.get_user_id
    )


def second_window():
    return Window(
        Const('Hello, it is second page!'),
        Button(Const('Get your Telegram ID'), 'button', callbacks.on_button_pressed),
        Back(Const('Back')),
        state=states.StartMenu.second_page
    )