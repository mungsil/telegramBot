import telegram
import asyncio
import schedule
import time
import pytz
import datetime
from openai import OpenAI

token = "6928016911:AAEfmD-uwp2jYpTxdN35vlI18BvqfpJ_x3M"
public_chat_name = "@kopensw"
bot = telegram.Bot(token=token)

async def send_message():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return

    ct = "current time = " + str(now)
    
    await bot.sendMessage(chat_id=public_chat_name, text=ct)

def job():
    asyncio.create_task(send_message())

async def main():
    schedule.every(30).minutes.do(job)
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
