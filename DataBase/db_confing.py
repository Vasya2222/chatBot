import sqlite3

PATH = 'DataBase/db_new_bot.db'

connect = sqlite3.connect(PATH)

cursor = connect.cursor()


def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS English_word
    (id INTEGER PRIMARY KEY AUTOINCREMENT, word_English VARCHAR NOT NULL, translate_word_on_Russian VARCHAR)''')
    connect.commit()


async def add_words(state):
    async with state.proxy() as data:
        cursor.execute('''INSERT OR IGNORE INTO English_word (word_English, translate_word_on_Russian) VALUES(?, ?)''', tuple(data.values()))
        connect.commit()


def game_words(random: tuple):
    ran = cursor.execute('''SELECT word_English FROM English_word WHERE id=?''', random).fetchall()
    return ran


def check_word(word_check: tuple):
    check = cursor.execute('''SELECT id FROM English_word WHERE translate_word_on_Russian=?''', word_check).fetchall()
    return check
