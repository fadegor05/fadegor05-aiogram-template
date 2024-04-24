from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from app.crud.user import get_user_by_telegram_id, create_user
from app.database import async_session
from app.dialogs.start.states import StartMenu
from app.handlers.router import router
from app.models.user import User


@router.message(CommandStart())
async def start_handler(message: Message, dialog_manager: DialogManager):
    async with async_session() as session:
        user: User = await get_user_by_telegram_id(session, message.from_user.id)
        if not user:
            user = await create_user(session, message.from_user.id)
        await message.answer(f'Hello, {message.from_user.first_name}, your id in DB is {user.id}!')

        await dialog_manager.start(StartMenu.first_page, mode=StartMode.RESET_STACK)


