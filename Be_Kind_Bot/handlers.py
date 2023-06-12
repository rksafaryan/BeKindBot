from main import bot, dp
from aiogram.types import Message
from config import admin_id
from model import check_rudeness


async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


@dp.message_handler()
async def echo(message: Message):
    if check_rudeness(message.text):
        await message.reply(text="Dont be rude!!! ")

