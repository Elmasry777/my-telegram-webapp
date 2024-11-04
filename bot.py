from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler

WEB_URL = "https://github.com/Elmasry777/TelegramBot.git/"

async def start(update: Update, context):
    user_id = update.message.from_user.id
    
    keyboard = [
        [InlineKeyboardButton("PLAY", url=f"{WEB_URL}?user_id={user_id}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        text="Welcome! Click the button below to start playing:",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token('7696140362AAHrLKz3owSNEuIljntItYDCsSZMrNP5X4c').build()

app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    app.run_polling()
