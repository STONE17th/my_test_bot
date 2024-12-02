from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command

handlers_router = Router()


@handlers_router.message(Command('start'))
async def on_start(message: Message, bot: Bot):
    await message.answer(
        f'Привет, {message.from_user.full_name}!',
    )


@handlers_router.message(Command('help'))
async def help_command(message: Message):
    print(f'{message.from_user.id} прислал {message.text}')
    await message.reply(
        f'{message.from_user.full_name} ТРЕБУЕТ ПОМОЩИ!'
    )
