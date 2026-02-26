import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message

API_TOKEN = "8723285400:AAHqJZVe3-6gXRB0FC-BucIYrI4LYCcw5u8"

AUTO_REPLY_TEXT = (
    "Если захотите присоединиться к буровому сообществу, "
    "то добро пожаловать: https://max.ru/join/SkMCiN_-agLAdrVQJQDSy8qo-jsE8tsdGjNG-vu-n54"
)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message()
async def send_link(message: Message):
    # Бот отвечает реплаем на ЛЮБОЕ сообщение, которое получает
    await message.reply(AUTO_REPLY_TEXT)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
