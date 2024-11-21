from aiogram import Bot, Dispatcher

import asyncio
import os

import callbacks
import handlers
import settings
from fsm import fsm_router

bot = Bot(token=os.getenv('MY_TOKEN'))
dp = Dispatcher()

dp.include_routers(
    handlers.command_router,
    callbacks.command_router,
    fsm_router,
)


async def start_bot():
    dp.startup.register(settings.start_up)
    dp.shutdown.register(settings.shut_down)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start_bot())
