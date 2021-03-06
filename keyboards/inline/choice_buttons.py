from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import buy_callback


choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Купить грушу', callback_data=buy_callback.new(
                item_name='pear', quantity=1
            )),
            InlineKeyboardButton(text='Купить яблоки', callback_data=buy_callback.new(
                item_name='apple', quantity=1
            )),
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data='cancel')
        ]
    ]
)
