from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command

handlers_router = Router()


@handlers_router.message(Command('start'))
async def on_start(message: Message, bot: Bot):
    await message.answer(
        f'Привет, {message.from_user.full_name}!',
    )
