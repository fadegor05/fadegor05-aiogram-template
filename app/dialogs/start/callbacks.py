from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button


async def on_button_pressed(c: CallbackQuery, widget: Button, manager: DialogManager):
    user_id = manager.middleware_data.get('event_chat').id
    await c.answer(f'You telegram id is {user_id}')