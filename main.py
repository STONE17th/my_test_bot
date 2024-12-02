from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

import asyncio
import os

from handlers import handlers_router

bot = Bot(os.getenv('BOT_TOKEN'))
dp = Dispatcher()

dp.include_routers(
    handlers_router,
)


def on_start():
    print('Bot is started!')


async def start_bot():
    dp.startup.register(on_start)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start_bot())
