import os
import json
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, ContextTypes, CommandHandler, MessageHandler, filters

TOKEN = os.environ.get("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN not found in environment!")

application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    greeting = "Добро пожаловать 👋\nЧтобы посмотреть прямой эфир, выберите канал ↓"
    
    keyboard = [
        [KeyboardButton("Матч! ТВ"), KeyboardButton("Матч! Футбол 1")],
        [KeyboardButton("Матч! Футбол 2"), KeyboardButton("Матч! Футбол 3")],
        [KeyboardButton("Матч! Боец")],
        [KeyboardButton("Fast Sports 🇦🇲"), KeyboardButton("Fast Sports 1 🇦🇲")],
        [KeyboardButton("Fast Sports 2 🇦🇲")],
        [KeyboardButton("Setanta Sports 1"), KeyboardButton("Setanta Sports 2")],
    ]
    
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(greeting, reply_markup=reply_markup)
    await update.message.reply_text("🔗 Ссылка на прямой эфир ниже\n👇 Нажмите кнопку, чтобы начать просмотр")
    await update.message.reply_text("🎰 Ставки на спорт 🎰")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    responses = {
        "Матч! ТВ": "https://example.com/match-tv (փոխիր իրականով)",
        "Матч! Футбол 1": "https://example.com/football1",
        "Матч! Футбол 2": "https://example.com/football2",
        "Матч! Футбол 3": "https://example.com/football3",
        "Матч! Боец": "https://example.com/boec",
        "Fast Sports 🇦🇲": "https://example.com/fast-sports",
        "Fast Sports 1 🇦🇲": "https://example.com/fast1",
        "Fast Sports 2 🇦🇲": "https://example.com/fast2",
        "Setanta Sports 1": "https://example.com/setanta1",
        "Setanta Sports 2": "https://example.com/setanta2",
    }
    
    reply = responses.get(text, "Ընտրիր կոճակներից մեկը վերևում 👆")
    await update.message.reply_text(reply)

application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

async def handler(event, context):
    try:
        body = json.loads(event["body"])
        update = Update.de_json(body, application.bot)
        await application.process_update(update)
        return {
            "statusCode": 200,
            "body": "ok"
        }
    except Exception as e:
        print("Error:", e)
        return {
            "statusCode": 500,
            "body": str(e)
        }
