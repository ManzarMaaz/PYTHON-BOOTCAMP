import pandas as pd
import random
import smtplib
import datetime as dt

# 🔒 Replace with your own email + app password
MY_EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"

# File paths
letters = [
    "letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt",
]
birthday_csv = "birthdays.csv"

# Read birthdays
birthdays_data = pd.read_csv(birthday_csv).to_dict(orient="records")

# Get today's date
today = dt.datetime.now()
day = today.day
month = today.month

# Check each person in the list
for person in birthdays_data:
    if day == person["day"] and month == person["month"]:
        random_letter = random.choice(letters)
        with open(random_letter, "r") as letter:
            updated_letter = letter.read().replace("[NAME]", person["name"])

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person["email"],
                msg=f"Subject: HAPPY BIRTHDAY 🎉\n\n{updated_letter}",
            )
