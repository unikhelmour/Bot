from aiogram import Dispatcher, Bot
import asyncio
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from config import TOKEN


bot = Bot(token=TOKEN)


dp = Dispatcher()

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer("Start")

@dp.message(Command("help"))
async def help(message:Message):
    await message.answer("Это раздел помощи")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())