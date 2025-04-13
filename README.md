# 🇰🇪 Kenya-Houses-Listing-Telegram-Bot 🏡🤖

This is a Python-powered automation project that scrapes the latest house listings from [BuyRentKenya](https://www.buyrentkenya.com/houses-for-sale) and sends the top 5 new listings every day to a Telegram bot. The bot shares the house title, price, location, and a link to the details page — all in one neat message, every morning at 10:00 AM.

## 📌 Features

- Scrapes real estate listings from BuyRentKenya.com
- Extracts house title, price, location, and link
- Sends top 5 latest listings to a Telegram bot
- Hosted and scheduled for daily updates using [PythonAnywhere](https://www.pythonanywhere.com/)

## 🛠️ Tech Stack

- Python 3
- `requests`, `beautifulsoup4` – for scraping
- `python-telegram-bot` – to send messages to Telegram
- `sqlite3` – to store the scraped data locally
- `csv` – optional storage format
- PythonAnywhere – cloud hosting and scheduling

## 🗂️ Project Structure

Kenya-Houses-Listing-Telegram-Bot/
├── buykenya.py           # Web scraper to collect latest listings
├── telegram_bot.py       # Telegram bot logic to send updates
├── houses_for_sale.csv   # Optional: CSV backup of listings
├── kenya_houses.db       # SQLite database storing listings
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation (this file)


---

## 🚀 Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/Sam-Analyst-code/Kenya-Houses-Listing-Telegram-Bot.git
cd Kenya-Houses-Listing-Telegram-Bot
```

2. **Create and activate a virtual environment (optional)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```
4. **Set up your Telegram bot**
- Create a bot via [BotFather](https://telegram.me/BotFather)
- Copy the token and set it in your code
- Add your chat ID

  5. **Start the bot manually**
  ```bash
  python telegram_bot.py
  ```


  ## Example Output
  ```rust
  📅 Latest Houses for Sale in Kenya:

1. 3 Bedroom Apartment - Ksh 7,500,000
📍 Kileleshwa, Nairobi
🔗 https://www.buyrentkenya.com/listings/example-1

2. 4 Bedroom Maisonette - Ksh 11,200,000
📍 South C, Nairobi
🔗 https://www.buyrentkenya.com/listings/example-2

...up to 5 listings
```



