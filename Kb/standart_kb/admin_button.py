
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_btn = ReplyKeyboardMarkup()

btn_add = KeyboardButton(text='/add')
btn_find = KeyboardButton(text='/find')
btn_delete = KeyboardButton(text='/delete')

admin_btn.add(btn_add, btn_find, btn_delete)
