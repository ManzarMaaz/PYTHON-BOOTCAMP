import time
import requests
import smtplib
import datetime as dt

my_mail = "your_email@gmail.com"
password = "your_app_password"
to_mail = "recipient_email@gmail.com"
my_latitude = "your_latitude"
my_longitude = "your_longitude"

# ---------------------------- ISS CHECK ------------------------------- #
def if_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])

    # Return True if ISS is within +5/-5 degrees of your location
    return abs(iss_latitude - my_latitude) <= 5 and abs(iss_longitude - my_longitude) <= 5

# ---------------------------- NIGHT CHECK ----------------------------- #
def if_night():
    parameters = {
        "lat": my_latitude,
        "lng": my_longitude,
        "tzid": "Asia/Kolkata",
        'formatted': 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunset = data['results']['sunset'].split('T')[1].split(':')[:2]
    sunrise = data['results']['sunrise'].split('T')[1].split(':')[:2]

    sunset_time = [int(sunset[0]), int(sunset[1])]
    sunrise_time = [int(sunrise[0]), int(sunrise[1])]

    now = dt.datetime.now()
    current_time = [now.hour, now.minute]

    return current_time > sunset_time or current_time < sunrise_time

# ---------------------------- SEND EMAIL ------------------------------ #
def send_mail():
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=to_mail,
            msg=f"Subject:ISS Alert\n\nHello, the ISS is above you in the sky!"
        )

# ---------------------------- MAIN LOOP ------------------------------- #
while True:
    if if_night() and if_overhead():
        send_mail()
    time.sleep(60)
