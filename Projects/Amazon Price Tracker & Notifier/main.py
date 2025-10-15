import os
import requests
import lxml
from bs4 import BeautifulSoup
from smtplib import SMTP
from dotenv import load_dotenv
load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
TARGET_EMAIL = os.getenv('TARGET_EMAIL')
EMAIL_PASSWORD =os.getenv('EMAIL_PASSWORD')
SMTP_ADDRESS = os.getenv('SMTP_ADDRESS')

PRODUCT_URL= "https://amzn.in/d/4zezZFo"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/", 
    "DNT": "1", 
    "Connection": "keep-alive"
}
response = requests.get(PRODUCT_URL, headers=headers)

response = requests.get(url=PRODUCT_URL, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

price = int(soup.find('span', class_='a-price-whole').getText().replace(',','').replace('.',''))
product_title = soup.find('span', id='productTitle').getText()

print(price)
print(product_title)

target_price = 70000

if price <= target_price:
    with SMTP(SMTP_ADDRESS, 587) as connection:
        connection.starttls()
        connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        email_subject = f"PRICE ALERT:{product_title[:25]}... is NOW {price:.2f} INR!"
        email_body = f"{product_title} is now {price:.2f} INR, which is below your target of {target_price:.2f} INR!\n\n"
        email_body += f"Click here to buy: {PRODUCT_URL}"
        
        # Construct the full message (subject and body)
        full_msg = f'Subject:{email_subject}\n\n{email_body}'
        
        connection.sendmail(
            from_addr=EMAIL_ADDRESS, 
            to_addrs=TARGET_EMAIL,
            msg=full_msg.encode('utf-8')
        )

    print(f"✅ Sent deal email to {TARGET_EMAIL}")
    print(full_msg)
