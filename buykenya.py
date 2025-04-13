import requests
from bs4 import BeautifulSoup
import sqlite3
import time

base_url = "https://www.buyrentkenya.com/houses-for-sale?page={}"
headers = {
    "User-Agent": "Mozilla/5.0"
}

# 1. Connect to SQLite and create the table
conn = sqlite3.connect('houses_for_sale.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS listings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        house_title TEXT,
        price TEXT,
        more_details_link TEXT,
        location TEXT
    )
''')

# 2. Start scraping and inserting
for page in range(1, 112):  # Pages 1 to 111
    print(f"Scraping page {page}...")
    response = requests.get(base_url.format(page), headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    listings = soup.select('div.flex.flex-col.justify-between.px-5.py-4.md\\:w-3\\/5')

    for listing in listings:
        title = listing.select_one('div > div > h2')
        link_tag = listing.select_one('div > div > h3 > a')
        location = listing.select_one('div > div > div > div > p')
        price_div = listing.find_next('div', class_='flex items-center justify-center text-xl font-bold leading-7 text-grey-900')
        price = price_div.get_text(strip=True) if price_div else None

        cursor.execute('''
            INSERT INTO listings (house_title, price, more_details_link, location)
            VALUES (?, ?, ?, ?)
        ''', (
            title.get_text(strip=True) if title else None,
            price,
            f"https://www.buyrentkenya.com{link_tag['href']}" if link_tag else None,
            location.get_text(strip=True) if location else None
        ))

    conn.commit()
    time.sleep(1)  # polite delay

conn.close()
print("✅ Scraping complete! Data saved to SQLite (houses_for_sale.db).")
