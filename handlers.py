from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, CallbackQuery
from aiogram.utils.formatting import as_list

from keyboards import ikb_fruit_message
from callback_data import FruitData

import bd

command_router = Router()


@command_router.message(Command('start'))
async def command_start(message: Message, command: CommandObject, bot: Bot):
    # data = list(map(lambda x: (x.split()[0], float(x.split()[1]), int(x.split()[2])), command.args.split(':')))

    await message.answer(
        f'Здравствуйте, господин!',
        # reply_markup=ikb_fruit_message(data),
    )


@command_router.callback_query(FruitData.filter(F.menu == 'fruit_price'))
async def inline_handler(callback: CallbackQuery, callback_data: FruitData, bot: Bot):
    msg = f'{callback_data.fruit}: {callback_data.price * callback_data.amount} рублей'
    await callback.answer(text=msg)


@command_router.callback_query(FruitData.filter(F.menu == 'cancel'))
async def inline_handler(callback: CallbackQuery, callback_data: FruitData, bot: Bot):
    # msg = f'{callback_data.fruit}: {callback_data.price * callback_data.amount} рублей'
    await callback.answer(text='Галя, у нас отмена!', show_alert=True)
# @command_router.message()
# async def location_handler(message: Message, bot: Bot):
#     print(message.from_user.id)
#     await message.answer(
#         f'Широта: {message.location.longitude}, Долгота: {message.location.latitude}'
#     )

# @command_router.message(F.text.in_({'1', '2', '3'}))
# async def hello_bye(message: Message, bot: Bot):
# # if message.text.lower() == 'привет':
# #     msg = 'И тебе привет!'
# # else:
# #     msg = 'Ну и иди...'
# # await message.answer(msg)
# await message.answer('И тебе привет!')
#
# @command_router.message(Command('add'))
# async def add_user(message: Message, bot: Bot, command: CommandObject):
# name, phone, comment = command.args.split()
# bd.insert_row(name, phone, comment)
# await message.answer(f'Пользователь {name} успешно добавлен!')
#
# @command_router.message(Command('get'))
# async def get_users(message: Message, bot: Bot, command: CommandObject):
# user_name = command.args
# db_data = bd.get_row(user_name, _all=True)
# content = as_list(
#     *db_data,
#     sep='\n' + '-' * 10 + '\n'
# )
# await message.answer(**content.as_kwargs())
#
# @command_router.message(Command('del'))
# async def del_user(message: Message, bot: Bot, command: CommandObject):
# user_id = command.args
# bd.delete_row(int(user_id))
# await message.answer(f'Пользователь {user_id} успешно добавлен!')

#
# @command_router.message(Command('help'))
# async def command_help(message: Message, bot: Bot):
#     await message.answer(f'Помоги себе сам')
#
#
# @command_router.message(Command('dice'))
# async def command_help(message: Message, bot: Bot):
#     result = await bot.send_dice(message.from_user.id)
#     await message.answer(f'У тебя выпало {result.dice.value}')
#
#
# @command_router.message(Command('get_id'))
# async def command_help(message: Message, bot: Bot):
#     await message.answer(str(message.from_user.id))
#     print(message.from_user.id)
#
#
# @command_router.message(Command('spam'))
# async def command_spam(message: Message, bot: Bot):
#     if message.from_user.id in settings.admins:
#         for user_id in settings.id_list:
#             await bot.send_message(
#                 text='СПАМ ДА И ТОЛЬКО!',
#                 chat_id=user_id,
#             )
#     else:
#         await message.answer(f'Соррян, {message.from_user.first_name} - ты не достоин СПАМить!')

# @dp.message()
# async def command_start(message: Message, bot: Bot):
#     await message.answer(f'Здарова, {message.from_user.first_name}!\nСам ты {message.text}')
