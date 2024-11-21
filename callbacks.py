from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message

command_router = Router()


@command_router.message(F.photo)
async def command_start(message: Message, bot: Bot):
    await message.answer('О, картинка!')
