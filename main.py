from aiogram import Dispatcher, Bot
from aiogram.types import Message
import logging
import asyncio
import dotenv

TOKEN=dotenv.dotenv_values('.env')['TOKEN']

async def echo(message: Message):
    await message.reply(message.text)

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.message.register(echo)

    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
