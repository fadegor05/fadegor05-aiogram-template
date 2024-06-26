import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram_dialog import setup_dialogs

from app.core.config import BOT_TOKEN
from app.database import db_init
from app.dialogs import get_dialogs
from app.handlers.router import router


async def main() -> None:
    await db_init()

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_routers(router, *get_dialogs())
    setup_dialogs(dp)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Stopped')