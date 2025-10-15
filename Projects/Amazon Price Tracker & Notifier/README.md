# 🛒 Amazon Price Tracker & Notifier

This Python script automates the process of tracking the price of any product on Amazon. It scrapes the product's webpage to get the current price and sends you an email notification if the price drops below a specified target. Never miss a deal again!



---

## ✨ Features

-   **Real-time Price Scraping**: Fetches the live price of a product from its Amazon URL.
-   **Automated Email Alerts**: Automatically sends a notification to your email address when the price drops below your target.
-   **Secure Credential Management**: Uses a `.env` file to safely store and access your email credentials, keeping them out of the source code.
-   **Customizable**: Easily change the product URL and target price directly in the script.
-   **Robust Scraping**: Utilizes custom headers to mimic a real browser request, reducing the chance of being blocked by Amazon.

---

## ⚙️ How It Works

1.  **Load Configuration**: The script starts by loading your email address, password, and target email from a secure `.env` file.
2.  **Fetch Product Page**: It sends an HTTP GET request to the specified Amazon product URL with specific user-agent headers to ensure a successful response.
3.  **Parse HTML**: The raw HTML of the product page is parsed using `BeautifulSoup` and the `lxml` parser to create a searchable object.
4.  **Extract Data**: The script finds and extracts the product's title and current price by locating the specific HTML tags and classes used by Amazon.
5.  **Compare Price**: The current price is compared against the `target_price` you have set.
6.  **Send Notification**: If the current price is less than or equal to your target price, the script connects to an SMTP server, logs in to your email account, and sends a formatted alert email to your target address with the deal details and a direct link to the product page.

---

## 🚨 Important Security Notice

This script is designed to work with a `.env` file for security. **Do not hardcode your email address or password directly into the script.**

-   Always use a **Google App Password** if you are using a Gmail account, not your main password.
-   Ensure your `.env` file is listed in your `.gitignore` file to prevent it from ever being committed to a public repository.

---

## 🛠️ Technology Stack

-   **Language**: Python 3
-   **Libraries**:
    -   `requests`: For making HTTP requests to the Amazon URL.
    -   `beautifulsoup4` & `lxml`: For parsing the HTML and extracting data.
    -   `smtplib`: For sending the email notification.
    -   `python-dotenv`: For managing environment variables securely.

---

## 🚀 Getting Started

### Prerequisites

-   Python 3.x installed.
-   An email account (e.g., Gmail) with an **App Password** generated for this script.

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/amazon-price-tracker.git](https://github.com/your-username/amazon-price-tracker.git)
    cd amazon-price-tracker
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required packages:**
    ```bash
    pip install requests beautifulsoup4 lxml python-dotenv
    ```

4.  **Create your environment file:**
    -   Create a new file named `.env` in the root directory of the project.
    -   Add your credentials and SMTP server details to this file:
    ```env
    EMAIL_ADDRESS="your_sending_email@gmail.com"
    TARGET_EMAIL="your_receiving_email@example.com"
    EMAIL_PASSWORD="your_16_digit_app_password"
    SMTP_ADDRESS="smtp.gmail.com"
    ```

5.  **Configure the script:**
    -   Open the `main.py` file.
    -   Update the `PRODUCT_URL` variable with the Amazon link of the product you want to track.
    -   Set the `target_price` variable to your desired price point.

### Usage

Run the script from your terminal:
```bash
python main.py
