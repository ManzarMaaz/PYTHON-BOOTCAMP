---

# 🏋️ Exercise Tracker with Nutritionix & Sheety

A Python application that allows users to log their daily exercises by simply typing what they did. The app calculates calories burned and other exercise details using **Nutritionix API** and automatically logs the data into a **Google Sheet** via **Sheety API**.

This project demonstrates practical **API integration, automation, and data tracking** in a real-world workflow.

---

## 🚀 Key Features

* Converts natural language exercise input into structured data using **Nutritionix API**.
* Logs exercise details including name, duration, and calories burned into a Google Sheet.
* Tracks date and time for each entry automatically.
* Simple, user-friendly interface — type what you did and let the app handle the rest.

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Libraries:** `requests`, `python-dotenv`, `datetime`
* **APIs:** Nutritionix, Sheety

---

## ⚙️ Setup & Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/exercise-tracker.git
   cd exercise-tracker
   ```

2. Install dependencies:

   ```bash
   pip install requests python-dotenv
   ```

3. Create a `.env` file with the following variables:

   ```
   NIX_APP_ID=your_nutritionix_app_id
   NIX_API_KEY=your_nutritionix_api_key
   SHEETY_ENDPOINT=your_sheety_endpoint
   SHEETY_USERNAME=your_sheety_username
   SHEETY_PASSWORD=your_sheety_password
   GENDER=your_gender
   WEIGHT_KG=your_weight_in_kg
   HEIGHT_CM=your_height_in_cm
   AGE=your_age
   ```

4. Run the script:

   ```bash
   python main.py
   ```

---

## 📩 Example Usage

```
Tell me which exercise(s) you did: ran 5 km and did 30 push-ups
Logged Running successfully!
Logged Push-Up successfully!
```

The corresponding Google Sheet will show:

* Date
* Time
* Exercise Name
* Duration (minutes)
* Calories burned

---

## 🤝 Contribution

Contributions and suggestions are welcome. Feel free to fork the repo, submit issues, or open pull requests.

---

## 📜 License

This project is licensed under the MIT License.

---
