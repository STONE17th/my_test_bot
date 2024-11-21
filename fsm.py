from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from bd import DataBase

fsm_router = Router()


class MyState(StatesGroup):
    name = State()
    phone = State()
    comment = State()


@fsm_router.message(Command('add'))
async def add_new_user(message: Message, state: FSMContext, bot: Bot) -> None:
    await state.set_state(MyState.name)
    await message.answer('Введите имя пользователя:')


@fsm_router.message(MyState.name)
async def add_new_user_name(message: Message, state: FSMContext, bot: Bot) -> None:
    await state.update_data(name=message.text)
    await state.set_state(MyState.phone)
    await message.answer('Введите телефон пользователя:')


@fsm_router.message(MyState.phone)
async def add_new_user_last_name(message: Message, state: FSMContext, bot: Bot) -> None:
    await state.update_data(phone=message.text)
    await state.set_state(MyState.comment)
    await message.answer('Введите комментарий пользователя:')


@fsm_router.message(MyState.comment)
async def add_new_user_last_name(message: Message, state: FSMContext, bot: Bot) -> None:
    await state.update_data(comment=message.text)
    await state.set_state(MyState.phone)
    data = await state.get_data()
    name = data['name']
    phone = data['phone']
    comment = data['comment']
    await message.answer(f'Новый пользователь:\n{name}: {phone} {comment}')
    DataBase().add_user(name, phone, comment)
    await state.clear()


@fsm_router.message()
async def all_message(message: Message, bot: Bot) -> None:
    await message.answer(f'Любое сообщение: {message.text}')
