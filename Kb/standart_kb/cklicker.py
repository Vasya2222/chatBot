from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.callback_query import CallbackQuery
from loader import dp

count = 0
kb_clicker = ReplyKeyboardMarkup()
kb_add = ReplyKeyboardMarkup()

btn_add = KeyboardButton(text='add_word')
btn_count = KeyboardButton(text=f"+1", callback_data="num_count")

btn_0 = KeyboardButton(text="-1")

kb_clicker.add(btn_count, btn_0)
kb_add.add(btn_add)



@dp.callback_query_handler(lambda c: c.data.startswith('num_count'))
async def on_keyboard_callback(callback_query):
    global count
    callback_data = callback_query.data
    button_state = callback_data.split('_')[-1]
    button_label = callback_data.split(' ')[-1]
    if button_state == 'count':
        count += 1
