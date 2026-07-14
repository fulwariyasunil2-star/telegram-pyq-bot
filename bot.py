import os
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🙏 Welcome to Rajasthan Exam PYQ Bot!\n\n"
        "जल्द ही यहाँ राजस्थान की सभी परीक्षाओं के PYQ उपलब्ध होंगे।",
        reply_markup=ReplyKeyboardRemove()
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    app.run_polling()
