import logging

from aiogram import Dispatcher, Bot, executor
from aiogram.types import Message, ParseMode

from config import BOT_TOKEN
from parser import get_posts, download_img_by_url

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def bot_start_handler(message: Message):
    await message.answer("Salom")


@dp.message_handler(commands=['news'])
async def bot_news_handler(message: Message):
    await message.answer("News")
    news = await get_posts()
    for item in news:
        context = f"<a href='{item['context']['url']}'><b>{item['title']}</b></a>\n\n" \
                  f"Bugun: {item['date']}\n\n" \
                  f"Korishlar soni: <em>{item['context']['views']}</em>"
        await message.answer_photo(photo=await download_img_by_url(item['img']), caption=context)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
