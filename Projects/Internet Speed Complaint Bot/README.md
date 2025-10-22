# 🤖 Automated Internet Speed Test & Complaint Bot

This Python script automatically tests your internet speed using Selenium and posts a public complaint to your internet provider on X (Twitter) if the speed is below a promised threshold.



---

## ✨ Features

-   **Selenium Automation**: Uses a Selenium-controlled Chrome browser to navigate `speedtest.net` in real-time.
-   **Dynamic Element Handling**: Reliably uses `WebDriverWait` to handle cookie consent pop-ups, the "GO" button, and the dynamically loading result fields.
-   **X (Twitter) API Integration**: Employs the `Tweepy` (v2 Client) to securely authenticate with the X API and post a tweet.
-   **Conditional Logic**: The core feature. It only posts a complaint *if* the measured download or upload speed is less than the promised speed.
-   **Secure Configuration**: Uses `python-dotenv` and a `.env` file to securely manage all API keys, access tokens, and the provider's X handle, keeping credentials out of the source code.
-   **Class-Based Design**: The logic is cleanly separated into two classes: `InternetSpeedBot` for Selenium operations and `TweepyClient` for API interactions.

---

## ⚙️ How It Works

1.  **Load Configuration**: The script starts by loading API credentials and the provider's X handle from the `.env` file.
2.  **Initialize `InternetSpeedBot`**: This class launches a Selenium browser, navigates to `speedtest.net`, and handles the cookie consent banner.
3.  **Run Speed Test**: The bot clicks the "GO" button and then enters a long `WebDriverWait` (90s) for the test to complete and the result elements to be populated.
4.  **Scrape Results**: Once the test is finished, the bot scrapes the final download and upload speed text from the page and then quits the browser.
5.  **Analyze Results**: The main script retrieves the `down_speed` and `up_speed` from the bot instance.
6.  **Initialize `TweepyClient`**: This class authenticates with the X API using the loaded credentials.
7.  **Tweet (If Necessary)**: The script compares the measured speeds to the `PROMISED_SPEED` constant. If either speed is too low, the `tweet_at_provider` method is called to construct and post the complaint tweet.

---

## 🛠️ Technology Stack

-   **Language**: Python 3
-   **Core Libraries**:
    -   `selenium`: For all browser automation and web element interaction.
    -   `tweepy`: A Python client for the X (Twitter) v2 API.
    -   `python-dotenv`: For managing environment variables securely.

---

## 🚀 Getting Started

### Prerequisites

-   Python 3.x
-   Google Chrome
-   `chromedriver` (Note: Modern versions of `selenium` often manage this automatically via Selenium Manager).
-   A Developer Account on X (Twitter) with **Write** (v2) or **Read & Write** (v1.1) permissions to generate API keys.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/internet-speed-bot.git](https://github.com/your-username/internet-speed-bot.git)
    cd internet-speed-bot
    ```

2.  **Install the required packages:**
    ```bash
    pip install selenium tweepy python-dotenv
    ```

3.  **Create your `.env` file:**
    -   Create a new file named `.env` in the root directory.
    -   Add your credentials. **The `INTERNET_PROVIDER` must be their X (Twitter) handle.**

    ```env
    # The X (Twitter) handle of your provider (e.g., "@ComcastCares" or "@MyISP_Support")
    INTERNET_PROVIDER="@YourProviderHandle"

    # Your X (Twitter) App's API Credentials
    CONSUMER_KEY="YOUR_CONSUMER_KEY"
    CONSUMER_SECRET="YOUR_CONSUMER_SECRET"
    ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
    ACCESS_TOKEN_SECRET="YOUR_ACCESS_TOKEN_SECRET"
    ```

4.  **Configure the `PROMISED_SPEED`:**
    -   Open the `main.py` file.
    -   Change the `PROMISED_SPEED = 30` constant to match the speed (in Mbps) your provider promised you.

### Usage

Run the script from your terminal. It will open a browser, run the test, and post to X if the speeds are unsatisfactory.

```bash
python main.py
```
## Example Console Output (Tweet Sent):
```bash
Opening Speedtest Website...
Cookie banner not found or skipped.
Please wait while we calculate the Internet Speed....
Wait is Over
Download Speed (Mbps): 18.50
Upload Speed (Mbps): 10.11
...
✅ Tweet posted successfully. Download speed (18.5 Mbps) is below 30 Mbps threshold.
```
## Example Console Output (No Tweet):
```bash
...
Wait is Over
Download Speed (Mbps): 32.80
Upload Speed (Mbps): 28.90
...
⏩ Speed is acceptable (Down: 32.8 Mbps). No tweet necessary.
```
