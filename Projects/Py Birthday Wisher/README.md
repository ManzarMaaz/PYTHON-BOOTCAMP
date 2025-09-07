# 🎂 Birthday Wisher 

This Python project automatically sends **personalized birthday wishes** to your friends and family via email.
It uses a CSV file to store birthdays, randomizes a letter template, and emails the greeting on the right day 🚀.

---

## 🔧 Features

* Stores birthdays in a CSV file.
* Checks every day if it’s someone’s birthday.
* Picks a **random letter template** and replaces `[NAME]` with the person’s real name.
* Sends the greeting automatically via Gmail SMTP.
* Easy to extend for multiple templates and recipients.

---

## 🗂️ Project Structure

```
📂 project-folder
 ┣ 📄 main.py
 ┣ 📄 birthdays.csv
 ┣ 📂 letter_templates
 ┃ ┣ 📄 letter_1.txt
 ┃ ┣ 📄 letter_2.txt
 ┃ ┗ 📄 letter_3.txt
 ┗ 📄 README.md
```

* **main.py** → Main script that checks birthdays and sends emails.
* **birthdays.csv** → List of people with `name`, `email`, `year`, `month`, `day`.
* **letter\_templates/** → Contains multiple greeting templates.
* **README.md** → Project documentation.

---

## 🚀 Getting Started

### 1. Clone this repository

```bash
git clone https://github.com/your-username/birthday-wisher.git
cd birthday-wisher
```

### 2. Install Python (>=3.7)

Check if Python is installed:

```bash
python --version
```

### 3. Set up Gmail App Password

1. Enable **2-Step Verification** in your Google account.
2. Go to **Google Account → Security → App passwords**.
3. Generate a password for "Mail".
4. Copy it and use it in place of your Gmail password in `main.py`.

### 4. Update birthdays.csv

Format:

```csv
name,email,year,month,day
Alice,alice@example.com,1995,7,14
Bob,bob@example.com,1990,12,3
```

### 5. Run the script

```bash
python main.py
```

---

## 🕒 Automating Daily Emails

* **Mac/Linux** → Use `cron` to run daily.
* **Windows** → Use Task Scheduler.

Example cron job (every morning at 9 AM):

```bash
0 9 * * * /usr/bin/python3 /path/to/main.py
```

---

## 📌 Example Output

**Email Subject:**

```
HAPPY BIRTHDAY 🎉
```

**Email Body:**

```
Dear Alice,

Wishing you a fantastic birthday full of love, joy, and cake 🎂!
```

---

## ✨ Future Improvements

* Add image or HTML email templates.
* Send reminders to yourself 1 day before someone’s birthday.
* Store birthdays in a database instead of CSV.

---

## 📜 License

This project is licensed under the MIT License.

---
