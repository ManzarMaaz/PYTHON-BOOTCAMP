# 📈 Stock Price & News Alert System

A Python-based automation tool that monitors stock price movements and delivers real-time alerts with the latest news updates via SMS.  
This project demonstrates practical integration of multiple APIs to build a useful, real-world application.  

---

## 🚀 Key Features
- Fetches daily stock data from the [Alpha Vantage API](https://www.alphavantage.co/).  
- Calculates percentage change between consecutive trading days.  
- Retrieves the latest 3 news articles related to the company from [NewsAPI](https://newsapi.org/).  
- Sends a concise SMS summary using [Twilio](https://www.twilio.com/) with:  
  - Stock movement indicator (🔺up / 🔻down).  
  - News headline and brief description.  

---

## 🛠️ Tech Stack
- **Language:** Python 3  
- **Libraries:** `requests`, `twilio`, `python-dotenv`  
- **APIs:** Alpha Vantage, NewsAPI, Twilio  

---

## ⚙️ Setup & Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/stock-news-alert.git
   cd stock-news-alert
2. Install dependencies:
  ```bash
  pip install requests twilio python-dotenv
  ```
4. Create a .env file and configure the following environment variables:
  ```bash
  STOCK_API=your_alpha_vantage_api_key
  NEWS_API=your_news_api_key
  TWILIO_ACCOUNT_SID=your_twilio_sid
  TWILIO_AUTH_TOKEN=your_twilio_auth_token
  MY_NUMBER=your_twilio_phone_number
  TO_NUMBER=receiver_phone_number
  ```
5. Run the script:
  ```bash
  python main.py

## 📩 Example SMS Alert
  ```bash
  TSLA: 🔺2%
  Headline: Tesla hits record production milestone
  Brief: Tesla achieved a new quarterly record in EV production and delivery.
  ```
## 🤝 Contribution
```bash
Contributions, suggestions, and improvements are welcome!
If you’d like to collaborate, feel free to open an issue or submit a pull request.
```
## 📜 License
```bash
This project is licensed under the MIT License.
```
