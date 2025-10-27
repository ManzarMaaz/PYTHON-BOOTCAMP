# 🏡 Zillow Form Automation Bot 🚀

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.0-green?logo=selenium&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-HTML%20Parser-orange?logo=html5&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

An intelligent automation bot that scrapes **property data** (address, price, links) from a Zillow-like real estate site 🏘️ and automatically fills it into a **Google Form** using Selenium.

Perfect for learning **web scraping**, **form automation**, and **data handling pipelines** — all in Python.

> ⚠️ **Disclaimer:**  
> This project is for **educational purposes only**. Always follow the target site's `robots.txt` and terms of service.

---

## 📑 Table of Contents

- [Features](#-features)
- [Workflow Diagram](#-workflow-diagram)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Impact / Learning](#-impact--learning)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)
- [Connect](#-connect)

---

## ✨ Features

- Scrapes property **price**, **address**, and **links** from a Zillow-clone website  
- Fills out a **Google Form automatically** with the scraped data  
- Uses **Selenium WebDriver** for browser automation  
- Integrates **BeautifulSoup** for structured HTML parsing  
- Cleanly loops through all entries and submits them sequentially  
- Designed for **hands-free data collection** 💪  

---

## 🧠 Workflow Diagram

```mermaid
flowchart TD
    A[Start Script] --> B[Send Request to Zillow Clone URL]
    B --> C[Parse HTML with BeautifulSoup]
    C --> D[Extract Addresses, Prices & Links]
    D --> E[Launch Chrome with Selenium]
    E --> F[Open Google Form]
    F --> G[Fill Each Entry in Form Fields]
    G --> H[Submit Form]
    H --> I{More Listings?}
    I -->|Yes| F
    I -->|No| J[Display Success Message & Quit Driver]
    J --> K[All Entries Submitted Successfully 🎉]
````

---

## 🧩 Tech Stack

* **Python 3.10+**
* **Requests** – for fetching web content
* **BeautifulSoup4** – for HTML parsing
* **Selenium** – for browser automation
* **Google Forms** – for data entry and logging

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ManzarMaaz/PYTHON-BOOTCAMP.git
cd PYTHON-BOOTCAMP/ZillowFormAutomation
```

Install dependencies:

```bash
pip install requests beautifulsoup4 selenium
```

---

## 🚀 Usage

1. Make sure you have **Google Chrome** and **ChromeDriver** installed.
2. Update the form link (`SHEET_URL`) in the script with your own Google Form URL.
3. Run the bot:

```bash
python main.py
```

4. Watch as it automatically opens the form and submits property details 🏠

---

## 🔍 How It Works

1. Sends an HTTP request to the target Zillow Clone page
2. Parses the HTML and extracts:

   * 🏡 Address
   * 💲 Price
   * 🔗 Property Link
3. Launches a browser window using Selenium
4. Fills each extracted entry into a Google Form
5. Submits and refreshes for the next record
6. Ends with a success message when all entries are submitted

---

## 💡 Impact / Learning

* Understanding **web scraping ethics** and HTML structure
* Automating browser tasks and form submissions
* Combining **Requests + BeautifulSoup + Selenium** for a full workflow
* Managing data extraction and entry automation efficiently

---

## 🔮 Future Enhancements

* Store scraped data in CSV or Google Sheets
* Add real Zillow integration with pagination handling
* Integrate error handling and retry logic
* Add headless mode for silent automation

---

## 📜 License

This project is licensed under the **MIT License** — see `LICENSE` for details.

---

## 🌐 Connect

👤 **Mohammed Manzar Maaz**
🔗 [LinkedIn Profile](https://www.linkedin.com/in/mohammed-manzar-maaz/)
💻 [GitHub Repository](https://github.com/ManzarMaaz/PYTHON-BOOTCAMP)

---

⭐ *If this project helped you learn web automation, don’t forget to star the repo!*


---
