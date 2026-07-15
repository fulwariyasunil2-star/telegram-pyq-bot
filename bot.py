import os
import threading
from flask import Flask
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()

app_web = Flask(__name__)

@app_web.route("/")
def home():
    return "Telegram Bot is Running!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🙏 Welcome to Rajasthan Exam PYQ Bot!\n\n"
        "जल्द ही यहाँ राजस्थान की सभी परीक्षाओं के PYQ उपलब्ध होंगे।",
        reply_markup=ReplyKeyboardRemove()
    )

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app_web.run(host="0.0.0.0", port=port)

def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    run_web()
