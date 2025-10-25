# 🏠 Zillow Data Automation Bot

This project automates the process of scraping property listings from a Zillow-style website and submitting them into a Google Form using Python.  

It demonstrates how **web scraping and automation** can work together to streamline data collection and entry tasks — ideal for data analysts, real estate researchers, or anyone who wants to reduce repetitive manual work.

---

## 🚀 Features

- Extracts property **addresses**, **prices**, and **links** from a Zillow-clone site  
- Automatically submits each listing to a **Google Form**  
- Uses **BeautifulSoup** for HTML parsing  
- Automates form filling with **Selenium WebDriver**  
- Includes **dynamic waits** for reliable interaction timing  
- Handles multiple entries seamlessly

---

## 🧩 Tech Stack

- **Python 3**
- **BeautifulSoup (bs4)**
- **Selenium**
- **Requests**
- **Google Forms**

---

## ⚙️ How It Works

1. Fetches the HTML content of the Zillow clone website using `requests`.  
2. Parses the data using `BeautifulSoup` to extract:  
   - Property address  
   - Price  
   - Listing link  
3. Launches Chrome with Selenium and navigates to the Google Form.  
4. Iterates through the listings and auto-fills the form fields one by one.  
5. Submits each entry and reloads the form for the next record.

---

## 📸 Workflow Overview

```plaintext
Fetch Data → Parse HTML → Extract Listings → Open Google Form → Auto-Fill Fields → Submit → Repeat
```

---

## 📂 Example Output

```
(Added) at Index: 3, Price: $2,850  
Address: 210 Elm Street, Denver, CO  
Link: https://www.zillow.com/homedetails/example

--- All entries submitted successfully! ---
```

---

## 🧠 Learning Highlights

- Automating repetitive data entry workflows  
- Understanding how Selenium interacts with dynamic web elements  
- Practical use of `WebDriverWait` for form reliability  
- Combining `requests` + `BeautifulSoup` for efficient web scraping  

---

## 🏁 Run the Project

```bash
pip install selenium beautifulsoup4 requests
python main.py
```

> 💡 *Make sure to log in to Chrome once manually if your form requires authentication.*

---

## 📌 Future Enhancements

- Integrate with Google Sheets API for direct submission  
- Add error handling and retry logic for form failures  
- Implement headless mode for faster execution

---

## 🔗 Connect & Explore

💻 **GitHub Repo:** [ManzarMaaz/PYTHON-BOOTCAMP](https://github.com/ManzarMaaz/PYTHON-BOOTCAMP)  
🌐 **LinkedIn:** [Mohammed Manzar Maaz](https://www.linkedin.com/in/mohammed-manzar-maaz/)

---

### ⭐ If you like this project, don’t forget to star the repo and share your thoughts!
