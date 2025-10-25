# 🤖 Instagram Followers Bot

This is a Python script that uses Selenium to automate following users on Instagram. The bot is designed to find a target account, open its list of followers, and follow a specified number of users from that list.

This project's primary purpose is to demonstrate Selenium's capabilities in navigating a complex, dynamic, and modern web application.



---

## 🚨 IMPORTANT: Disclaimer & Warnings

1.  **Against Terms of Service**: Automating interactions on Instagram is **a direct violation of their Terms of Service**. This script is intended purely as a technical demonstration. Running this script can easily lead to your account being rate-limited, action-blocked, or **permanently suspended**. Use at your own risk.
2.  **Extremely Brittle Selectors**: Instagram's class names (e.g., `x1qnrgzn...`) are auto-generated and change frequently. This script **will break** with any Instagram UI update. It is a proof-of-concept, not a production-ready tool.

---

## ✨ Features

-   **Browser Automation**: Uses `selenium.webdriver` to launch and control a Chrome browser.
-   **Persistent Session**: Leverages the `--user-data-dir` Chrome option to save and reuse a browser profile. This allows you to log in manually *once* and have the bot use that session for all future runs, bypassing the need to automate the login process.
-   **Targeted Search**: Automatically navigates the search UI to find a specific target account.
-   **Follower List Navigation**: Clicks the "followers" link to open the dynamic-scrolling modal.
-   **Automated Follow Loop**: Iterates through the follower list and clicks the "Follow" button up to a set limit (15).

---

## ⚙️ How It Works

1.  **Launch Browser**: The script launches a new Chrome window using a local folder named `chrome_profile` to store session data.
2.  **Search for Account**: The bot clicks the "Search" icon, types the `ACCOUNT_NAME` into the search bar, and hits `ENTER`.
3.  **Open Account**: It waits and clicks on the correct account from the search results to navigate to their profile page.
4.  **Open Followers Modal**: It finds and clicks the "followers" link, which opens the pop-up list.
5.  **Follow Loop**: The script gets a list of all users in the modal. It then loops through this list:
    -   It checks the text of the button for each user.
    -   If the text is "Follow" and the bot hasn't already followed its limit (15), it clicks the button.
    -   It adds a 3-second delay between follows to mimic human behavior (though this is not a reliable way to avoid detection).
6.  **Completion**: Once 15 accounts are followed, the script prints a completion message and quits.

---

## 🛠️ Technology Stack

-   **Language**: Python 3
-   **Core Library**: `Selenium`
-   **Standard Libraries**: `os`, `time`

---

## 🚀 Getting Started

### Prerequisites

-   Python 3.x
-   Google Chrome
-   `chromedriver` (Note: Modern versions of `selenium` often manage this automatically via Selenium Manager).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/instagram-followers-bot.git](https://github.com/your-username/instagram-followers-bot.git)
    cd instagram-followers-bot
    ```

2.  **Install the required packages:**
    ```bash
    pip install selenium
    ```

### **One-Time Manual Setup (Crucial!)**

This bot uses a persistent profile to avoid handling login credentials. You must set this up once.

1.  **Run the script:** `python main.py`
2.  A new Chrome window will open. **Manually log in to your Instagram account** in this window.
3.  Once you are logged in, **close the browser window**.
4.  Your session data is now saved in the new `chrome_profile` directory.

### Usage

After completing the one-time setup, simply run the script from your terminal whenever you want:

```bash
python main.py
```
The bot will now use your saved session to run as an authenticated user. You can change the target account by modifying the ACCOUNT_NAME variable in the script.
