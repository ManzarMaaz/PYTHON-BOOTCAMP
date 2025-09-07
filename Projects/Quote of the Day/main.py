import random
import smtplib
import datetime as dt

my_mail='any_working_mail'
password="app_password"

now = dt.datetime.now()
today = now.weekday()

with open('DAY 32/Birthday Wisher (Day 32) start/quotes.txt', 'r') as file:
    quotes_list = file.readlines()

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        if today in [0,1,2,3,4,5,6]:
            connection.sendmail(from_addr=my_mail,
                            to_addrs='receiver_mail',
                            msg=f'subject:Quote of the Day\n\n{random.choice(quotes_list)}')
