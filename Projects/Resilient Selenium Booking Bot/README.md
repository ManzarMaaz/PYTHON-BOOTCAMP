# 🤖 Resilient Selenium Booking Bot

This project is an advanced Python script that uses Selenium to automate booking classes on a demonstration gym website. The bot is designed from the ground up for **resilience and reliability**.

Its core feature is a custom-built retry mechanism that intelligently handles common web automation failures (like network lag, slow-loading elements, and `StaleElementReferenceException`), ensuring the script runs to completion even on an unreliable network.



---

## ✨ Key Features

-   **Resilient Retry Wrapper**: A custom `retry()` function wraps all critical Selenium actions. It automatically re-attempts failed operations (e.g., clicks, element lookups) up to 7 times, gracefully handling `TimeoutException`, `NoSuchElementException`, and `StaleElementReferenceException`.
-   **End-to-End Test Flow**: The bot executes a full user journey:
    1.  **Login**: Securely logs into the user account.
    2.  **Filter & Select**: Parses the schedule and identifies target classes (e.g., "Tuesday/Thursday at 6:00 PM").
    3.  **Act**: Clicks the "Book" or "Join Waitlist" button.
    4.  **Verify Action**: *Confirms* the booking was successful by waiting for the button text to change to "Booked" or "Waitlisted".
    5.  **Final Verification**: Navigates to the "My Bookings" page to cross-check that all attempted bookings are present.
-   **Advanced Selenium Techniques**: Relies 100% on explicit `WebDriverWait` and `expected_conditions` (including custom `lambda` waits) to interact with elements efficiently, avoiding all `time.sleep()` calls for flow control.
-   **Modular Functions**: Each major step (Login, Booking, Verification) is encapsulated in its own clean, reusable function.
-   **Session Persistence**: Utilizes a Chrome User Data Directory (`--user-data-dir`) to maintain the login session between script runs, simplifying debugging and re-runs.

---

## ⚙️ How It Works

1.  **Initialization**: The script launches a Selenium-controlled Chrome browser with a persistent user profile.
2.  **Resilient Login**: It calls `perform_login()`, which is wrapped by the `retry()` function. If the login page is slow to load or an element is not immediately available, the function will retry the entire login process.
3.  **Class Scheduling Loop**:
    -   The script scrapes the main schedule and finds all class cards.
    -   It filters these cards based on the desired criteria (day and time).
    -   For each matching class, it calls `perform_booking_action()`.
4.  **Resilient Booking Action**:
    -   The `perform_booking_action()` function clicks the "Book" button.
    -   It then *immediately* starts an explicit wait (`wait.until(lambda d: button.text in ["Booked", "Waitlisted"])`). This is the critical step: it waits for the server to respond and the UI to update.
    -   If the UI doesn't update within the `RETRY_TIMEOUT`, the `retry` wrapper catches the `TimeoutException` and re-attempts the click.
5.  **Final Verification**:
    -   After processing all classes, the bot calls `get_my_bookings_cards()`.
    -   This function navigates to the "My Bookings" page and retrieves all confirmed booking cards, again using the `retry` wrapper for stability.
6.  **Report**: The script prints a final summary to the console, comparing the number of new bookings to the list of verified bookings found on the "My Bookings" page.

---

## 💡 Core Concept: The `retry()` Wrapper

The most valuable component of this project is the `retry()` function. This design pattern is essential for building stable automation in real-world environments where networks are not perfect and front-ends are dynamic.

-   It takes a function (an "action") as an argument.
-   It executes the action in a `try...except` block.
-   On success, it returns the result.
-   On failure (catching specific Selenium exceptions), it logs the failure and waits for a brief, randomized period before trying again.
-   If it fails all attempts, it raises the last exception, failing the script predictably.

This approach transforms a flaky, unreliable script into a robust automation tool.

---

## 🛠️ Technology Stack

-   **Language**: Python 3
-   **Core Library**: `Selenium`
-   **Standard Libraries**: `os`, `time`, `random` (for jitter in the retry logic)

---

## 🚀 Getting Started

### Prerequisites

-   Python 3.x
-   Google Chrome
-   `chromedriver` (Note: Modern versions of `selenium` often manage this automatically via Selenium Manager).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/resilient-selenium-bot.git](https://github.com/your-username/resilient-selenium-bot.git)
    cd resilient-selenium-bot
    ```

2.  **Install the required packages:**
    ```bash
    pip install selenium
    ```

### Usage

The script is configured with test credentials and a target URL. Simply run the script from your terminal:

```bash
python main.py
```
## 📋 Example Output
The console output provides a real-time log of the bot's actions. Note how it clearly shows the retry() wrapper successfully handling one failed attempt on the first class and two failed attempts on the second class, all without crashing the script.

```bash
✅ Login successful on attempt 1/5.
✅ Logged in Successfully !!!

--- Processing: Spin Class on Today (Tue, Oct 21) (Time: 6:00 PM) ---
🔄 Class Action failed on attempt 1/5. Retrying...
✅ Class Action successful on attempt 2/5.
✅ Successfully Booked: Spin Class on Today (Tue, Oct 21)

--- Processing: Spin Class on Thu, Oct 23 (Time: 6:00 PM) ---
🔄 Class Action failed on attempt 1/5. Retrying...
🔄 Class Action failed on attempt 2/5. Retrying...
✅ Class Action successful on attempt 3/5.
✅ Successfully Booked: Spin Class on Thu, Oct 23

-------BOOKING SUMMARY--------
New Bookings: 2
New Waitlist Entries: 0
Already Booked/ Waitlisted: 0
Total Tuesday & Thursday 6pm classes: 2

-------DETAILED CLASS LIST--------
- [New Bookings] Spin Class on Today (Tue, Oct 21)
- [New Bookings] Spin Class on Thu, Oct 23
✅ Retrieve My Bookings successful on attempt 1/5.

-------Verifying on my Bookings Page----
✅ Verified: Spin Class
✅ Verified: Spin Class

Expected Bookings (New/Waitlist): 2
Found Bookings: 2
```
