# ISS Overhead Notifier (Python Project)

This Python script notifies you by email whenever the International Space Station (ISS) is passing overhead at your location **and** it is nighttime, so the ISS is visible.

---

## Features
- Tracks the ISS position in real time using the [Open Notify API](http://api.open-notify.org/iss-now.json)  
- Gets local sunrise and sunset times from the [Sunrise-Sunset API](https://sunrise-sunset.org/api)  
- Checks if the ISS is within 5 degrees of your location and whether it’s dark outside  
- Sends an email alert if conditions are met  

---

## Tech Stack
- Python 3  
- `requests` for API calls  
- `smtplib` for sending emails  
- `datetime` for time handling  

---

## Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/iss-overhead-notifier.git
   cd iss-overhead-notifier

Install requirements:
pip install requests

Update the following variables in main.py with your own details:
```
my_mail = "your_email@gmail.com"
password = "your_app_password"
to_mail = "recipient_email@gmail.com"
my_latitude = "your_latitude"
my_longitude = "your_longitude"
```

Note: For Gmail, you need to create an App Password instead of using your main password.

Run the script:
```
python main.py
```

## What I Learned
```markdown
- Using multiple APIs in a single project  
- Sending automated emails with Python and SMTP  
- Writing scripts that run continuously and check conditions in real time  
```
## Future Improvements
```
- Integrate with SMS or push notifications  
- Build a Tkinter GUI version for easy setup  
- Deploy as a background service or cron job  

