import json
from dotenv import load_dotenv
import requests
import os
from twilio.rest import Client

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API = os.getenv("NEWS_API")
STOCK_API = os.getenv("STOCK_API")

stock_parameters = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'apikey':STOCK_API
}

stock_url = (f'https://www.alphavantage.co/query?')
r = requests.get(url=stock_url, params=stock_parameters)
r.raise_for_status()
print(r.status_code)

stock_data = r.json()['Time Series (Daily)']

dates = sorted(stock_data.keys(), reverse=True)
yesterday = dates[0]
db_yesterday = dates[1]

y_stock = float(stock_data[yesterday]['4. close'])
dby_stock = float(stock_data[db_yesterday]['4. close'])

perc_diff = ((y_stock - dby_stock)/dby_stock) * 100 
print(f'Stock Change: {perc_diff:.2f}%')

news_parameters = {
    'q':COMPANY_NAME,
    'from':str(db_yesterday),
    'to':str(yesterday),
    'sortBy':'popularity',
    'apiKey' : NEWS_API
}

my_num = os.getenv("MY_NUMBER")
to_num = os.getenv("TO_NUMBER")
account_sid= os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")


client = Client(account_sid, auth_token)

news_url = ('https://newsapi.org/v2/everything?')

r_news = requests.get(url=news_url, params=news_parameters)
r_news.raise_for_status()
print(r_news.status_code)

news_data = r_news.json()
article = news_data['articles'][0]

arrow = '🔺' if perc_diff > 0 else '🔻'

headline = (article['title'][:50] + "...") if len(article['title']) > 50 else article['title']
brief = (article['description'][:80] + "...") if article['description'] and len(article['description']) > 80 else article['description']

body = (
    f"{STOCK}: {arrow}{abs(int(perc_diff))}%\n"
    f"Headline: {headline}\n"
    f"Brief: {brief}"
)

message = client.messages.create(
    body=body,
    from_=my_num,
    to=to_num,
)

print(message.status)
print(message.body)

