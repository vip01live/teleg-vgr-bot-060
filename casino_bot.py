import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("8583042031:AAG9b8oALRGGcnd-Xih63NRYLRuCe8AizDw")

async def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    user_name = user.first_name if user.first_name else "Ընկեր"
    
    message_text = f"""
🎰 Բարի գալուստ {user_name}

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
    
    keyboard = [[InlineKeyboardButton("🎰 ՍՏԱՆԱԼ 🎰", url="https://t.me/VGR060Bot/casino")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        text=message_text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    print("🤖 Բոտը գործարկված է...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
