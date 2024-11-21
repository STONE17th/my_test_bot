from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonRequestUser

from callback_data import FruitData


def ikb_fruit_message(data: list[tuple[str, float, int], ...]):
    keyboard = InlineKeyboardBuilder()
    for fr, pr, am in data:
        keyboard.button(
            text=fr,
            callback_data=FruitData(
                menu='fruit_price',
                fruit=fr,
                price=pr,
                amount=am,
            ),
        )
    keyboard.button(
        text='Отмена',
        callback_data=FruitData(
            menu='cancel',
        )
    )
    keyboard.adjust(*([2] * (len(data) // 2) + [1]))
    return keyboard.as_markup()

# def ikb_cancel():
#     keyboard = InlineKeyboardBuilder()
#     keyboard.button(
#         text='Отмена',
#         callback_data=FruitData(
#             menu='cancel',
#         )
#     )
