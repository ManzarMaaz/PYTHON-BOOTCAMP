# 🍪 Selenium Cookie Clicker Bot

This is a Python script that uses Selenium to automatically play the web game "Cookie Clicker." The bot clicks the big cookie as fast as possible and implements a "greedy" purchasing algorithm to buy the most expensive available upgrade every 10 seconds.



---

## ✨ Features

-   **Browser Automation**: Uses `selenium.webdriver` to launch and control a Chrome browser.
-   **Dynamic Element Handling**: Employs `WebDriverWait` to reliably wait for elements like the language selector and the big cookie to become clickable.
-   **High-Speed Clicking**: Enters a `while` loop to click the main cookie as fast as the browser can register.
-   **Smart Purchasing Strategy**: Every 10 seconds, the bot:
    1.  Checks its current cookie count.
    2.  Scans for all unlocked and available (enabled) products.
    3.  Buys the **most expensive** affordable upgrade to maximize cookie production.
-   **Timed Execution**: The script runs for a configurable amount of time (default is 1 minute) before printing the final score and closing the browser.

---

## ⚙️ How It Works

1.  **Launch & Setup**: The script launches a new, detached Chrome browser window and navigates to the Cookie Clicker game URL. It maximizes the window.
2.  **Language Selection**: It waits for the "English" language option to appear and clicks it.
3.  **Start Clicking**: It locates the "Big Cookie" element and begins clicking it in a continuous loop.
4.  **Purchase Loop**: The bot has a secondary timer. Every `WAIT_TIME` (10 seconds):
    -   It gets the current number of cookies.
    -   It finds all products that are both `.unlocked` and `.enabled`.
    -   It reverses this list to start with the most expensive items first.
    -   It clicks the first item in the list (the best one it can afford) to purchase it.
    -   It then resumes clicking the big cookie.
5.  **Game Over**: After `ONE_MINUTE` (60 seconds) has passed, the loop breaks. The script prints the final cookie count from the game and then quits the browser session.

---

## 🛠️ Technology Stack

-   **Language**: Python 3
-   **Libraries**:
    -   `selenium`: For all browser automation and web element interaction.
    -   `time`: To manage the purchasing timers and the total script runtime.

---

## 🚀 Getting Started

### Prerequisites

-   Python 3.x
-   Google Chrome browser
-   `chromedriver` (In recent versions of Selenium, this is often managed automatically by Selenium Manager. If not, you may need to [download it](https://googlechromelabs.github.io/chrome-for-testing/) and ensure it's in your system's PATH.)

### Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/cookie-clicker-bot.git](https://github.com/your-username/cookie-clicker-bot.git)
    cd cookie-clicker-bot
    ```

2.  **Install the required packages:**
    ```bash
    pip install selenium
    ```

3.  **Run the script:**
    ```bash
    python main.py
    ```
    The script will open a new Chrome window and begin playing. Watch the console to see its purchase decisions in real-time!

### Configuration

You can easily adjust the bot's behavior by changing the constants at the top of the `main.py` file:
-   `WAIT_TIME`: How often (in seconds) the bot checks for upgrades.
-   `ONE_MINUTE`: The total duration (in seconds) the bot will run for.
