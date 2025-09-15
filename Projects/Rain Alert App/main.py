from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client

# load .env file
load_dotenv()

my_lat = os.getenv("MY_LATITUDE")
my_long = os.getenv("MY_LONGITUDE")
my_api = os.getenv("API")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
my_num = os.getenv("MY_NUMBER")
to_num = os.getenv("TO_NUMBER")


response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={my_lat}&lon={my_long}&appid={my_api}&cnt=4")

response.raise_for_status()

print(response.status_code)

data = response.json()

will_rain = False

for y in range(4):
    weather_id = data['list'][y]['weather'][0]['id']

    if weather_id < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Hey, It Might Rain Today ☔️🌧️",
        from_=my_num,
        to=to_num,
    )

    print(message.status)
    print(message.body)