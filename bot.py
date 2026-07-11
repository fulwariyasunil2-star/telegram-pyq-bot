from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = 8864004884:AAEaTJXLOlrZg5fuWizAJCt7z_o1vLX4Fi4

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🙏 Welcome to Rajasthan Exam PYQ Bot!\n\n"
        "जल्द ही यहाँ राजस्थान की सभी परीक्षाओं के PYQ उपलब्ध होंगे।"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
