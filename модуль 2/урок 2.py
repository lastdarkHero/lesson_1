from telebot import TeleBot
import random
from telebot.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

bot = TeleBot("5471370817:AAHYo0DTG-7MVNfqfKlZZDi033cNq59eaWs")
BASE_FILES_DIR = r"C:\Users\Админ\PycharmProjects\29\lesson_2\extra"


def create_welcome_keyboard():
    welcome_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_1 = KeyboardButton("/cats")
    button_2 = KeyboardButton("/poem")
    button_3 = KeyboardButton("/music")
    button_4 = KeyboardButton("/sticker")
    welcome_keyboard.add(button_1, button_2, button_3, button_4)
    return welcome_keyboard


@bot.message_handler(commands=['start', 'help'])
def welcome(message: Message):
    welcome_keyboard = create_welcome_keyboard()
    bot.send_message(message.from_user.id, "Привет, выбери команду!", reply_markup=welcome_keyboard)


@bot.message_handler(commands=['cats'])
def cats(message: Message):
    random_img_number = random.randint(1, 9)
    random_img = open(rf"{BASE_FILES_DIR}\{random_img_number}.jpg", "rb")
    bot.send_photo(message.from_user.id, random_img)


@bot.message_handler(commands=['music'])
def music(message: Message):
    audio = open(fr"{BASE_FILES_DIR}\happy.mp3", "rb")
    bot.send_audio(message.from_user.id, audio)


@bot.message_handler(commands=['poem'])
def poem(message: Message):
    bot.send_message(message.from_user.id, "Села муха на варенье, вот и всё стихотворенье.")
    poem_keyboad = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton("Перейти", url="https://stihi.ru/")
    poem_keyboad.add(button)
    bot.send_message(message.from_user.id, "Больше стихотворений здесь:", reply_markup=poem_keyboad)


@bot.message_handler(commands=['sticker'])
def sticker(message: Message):
    bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAEG6g5joeQk_Nk336YDlZx-glR_v7haXQACZicAAnJPEUmPNUF-oX8pGywE")


bot.polling()
