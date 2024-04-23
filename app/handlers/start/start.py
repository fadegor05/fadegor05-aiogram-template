from aiogram.filters import CommandStart
from aiogram.types import Message

from app.handlers.router import router


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Hello, World!")
