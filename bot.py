from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os
BOT_TOKEN = os.getenv("8583042031:AAG9b8oALRGGcnd-Xih63NRYLRuCe8AizDw")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    first_name = update.effective_user.first_name

    text = f"""
🎰 Բարի գալուստ {first_name}

Պատրա՞ստ ես փորձել քո բախտը և բացել մեծ շահումների դուռը 💰

🎁 Քեզ սպասում է՝
🔥 50 FREE SPINS
🔥 500% բոնուս առաջին դեպոզիտի վրա

✅ Առանց անձնագրի
✅ Առանց հաստատման
✅ Միայն նոր օգտվողների համար

⚠️ ՇԱՏ ԿԱՐԵՎՈՐ
Բոնուսը և հաղթելու հնարավորությունը ակտիվանում են
միայն եթե օգտագործես պրոմոկոդը 👇

🎯 ՊՐՈՄՈԿՈԴ՝ VGR060
"""

    keyboard = [
        [InlineKeyboardButton("🎰 ՍՏԱՆԱԼ 🎰", url="https://t.me/VGR060Bot/casino")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(text, reply_markup=reply_markup)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
