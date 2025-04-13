import sqlite3
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Telegram token
TELEGRAM_TOKEN = 'MY TOKEN'

# Function to get latest 5 listings
def get_latest_houses():
    conn = sqlite3.connect('houses_for_sale.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT house_title, price, location, more_details_link 
        FROM listings 
        ORDER BY id DESC 
        LIMIT 5
    ''')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Telegram command handler
async def latest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    listings = get_latest_houses()

    if not listings:
        await update.message.reply_text("No house listings found.")
        return

    for house in listings:
        title, price, location, link = house
        message = (
            f"🏠 *{title}*\n"
            f"💰 *Price:* {price}\n"
            f"📍 *Location:* {location}\n"
            f"🔗 [View Details]({link})"
        )
        await update.message.reply_markdown(message)

# Start handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome! Send /latest to get the latest 5 houses for sale.")

# Run the bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("latest", latest))
    print("🚀 Bot is running...")
    app.run_polling()
