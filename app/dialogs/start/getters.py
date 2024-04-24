from aiogram_dialog import DialogManager


async def get_user_id(dialog_manager: DialogManager, **kwargs):
    return {
        'telegram_id': dialog_manager.middleware_data.get('event_chat').id
    }
