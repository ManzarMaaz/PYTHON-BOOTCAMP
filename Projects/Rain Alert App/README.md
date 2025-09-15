# ☔ Rain Alert App

A Python automation script that checks the **weather forecast** using the [OpenWeather API](https://openweathermap.org/api) and sends an **SMS alert** if rain is predicted — powered by [Twilio](https://www.twilio.com/).

---

## 🔑 Features
```markdown
- 🌤 Fetches weather forecast for your location  
- 📡 Uses OpenWeather API (free tier works fine)  
- 📱 Sends SMS alerts with Twilio if rain is likely  
- 🔐 Environment variables handled securely with `.env`  
```
---

## 🛠️ Tech Stack
```markdown
- **Python 3**  
- **Libraries:** `requests`, `twilio`, `python-dotenv`  
- **APIs:** OpenWeather API, Twilio SMS API  
```
---

## 🚀 Setup Instructions

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/rain-alert-app.git
   cd rain-alert-app
   ```

2. Install dependencies:

   ```bash
   pip install requests twilio python-dotenv
   ```

3. Create a `.env` file in your project root and add your credentials:

   ```ini
   MY_LATITUDE=your_lat
   MY_LONGITUDE=your_long
   API=your_openweather_api_key
   TWILIO_ACCOUNT_SID=your_twilio_sid
   TWILIO_AUTH_TOKEN=your_twilio_token
   MY_NUMBER=your_twilio_phone_number
   TO_NUMBER=recipient_phone_number
   ```

4. Run the script:

   ```bash
   python main.py
   ```

---

## 📚 What I Learned
```markdown
* How to work with **weather APIs**
* Sending **SMS programmatically** with Twilio
* Managing credentials securely with `.env` files
```
---

## 🚀 Future Improvements
```markdown
* Add **email notifications** as an alternative
* Extend to **7-day forecasts**
* Build a simple **GUI or mobile app version**
```
---
⭐ If you like this project, give it a star and try it out!
