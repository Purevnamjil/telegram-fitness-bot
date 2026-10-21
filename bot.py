import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Лог тохируулах
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")  # Сервер дээр ажиллах нууц түлхүүр
MY_CHAT_ID = os.getenv("CHAT_ID")  # Таны Telegram ID (Зөвхөн танд л мессеж явуулах зорилгоор)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    await update.message.reply_text(
        f"Сайн уу Пүүжээ! Чиний фитнесс болон хоолны сануулагч бот идэвхжлээ. 🚀\nТаны Chat ID: {user_id}"
    )

# Өглөөний сануулагч (Жишээ нь өглөөний 08:00 цагт)
async def morning_routine(context: ContextTypes.DEFAULT_TYPE):
    if MY_CHAT_ID:
        await context.bot.send_message(
            chat_id=MY_CHAT_ID,
            text="☀️ Өглөөний мэнд Пүүжээ!\n- 3 шарсан өндөг 🍳\n- 1 зүсэм бор талх 🍞\n- Сүүтэй кофе ☕\nӨдрөө сайхан эхлүүлээрэй!"
        )

# Оройн аарц сануулагч (Жишээ нь оройн 20:00 цагт)
async def evening_routine(context: ContextTypes.DEFAULT_TYPE):
    if MY_CHAT_ID:
        await context.bot.send_message(
            chat_id=MY_CHAT_ID,
            text="🌙 Оройн мэнд!\n- 250 гр шингэн аарцаа ууж сэргэлтээ дэмжээрэй! 🥛💪"
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    # Цагийн хуваарь тохируулах (APScheduler ашиглан автоматаар цагт нь явуулах)
    scheduler = AsyncIOScheduler()
    
    # Жишээ нь өдөр бүр Улаанбаатарын цагаар өглөө 08:00 болон орой 20:00 цагт ажиллана
    # (Цагийн бүсээ server дээр UTC-ээр тооцох эсвэл цагаа тааруулж болно)
    scheduler.add_job(morning_routine, 'cron', hour=8, minute=0, args=[app])
    scheduler.add_job(evening_routine, 'cron', hour=20, minute=0, args=[app])
    
    scheduler.start()

    print("Бот амжилттай аслаа...")
    app.run_polling()

if __name__ == '__main__':
    main()
