from aiogram import Bot

from itertools import chain


id_list = [
    814910816,
    438414297,
    626841737,
    6691080727,
    499907984,
]

admins = {
    409205647,
    118781425,
}


def start_up():
    print('Bot is started')


async def shut_down(bot: Bot):
    # for user_id in chain(id_list, admins):
    #     await bot.send_message(
    #         text='Бот прилег',
    #         chat_id=user_id,
    #     )
    print('Bot is stopped!')
