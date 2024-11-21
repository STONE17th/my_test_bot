from aiogram.filters.callback_data import CallbackData


class FruitData(CallbackData, prefix='FD'):
    menu: str
    fruit: str = ' '
    price: float = 0
    amount: int = 0
