# ✈️ Flight Club

An automated flight deal finder that notifies a club of users via email and SMS.

This project, **Flight Club**, is an enhanced application that automates the search for cheap flights. It features logic for **indirect flights**, sends personalized **email notifications** to a member list, and uses **INR (₹)** as its primary currency. The application tracks destinations from a Google Sheet and alerts all club members when a flight price drops below a set target.



---

## ✨ Key Features

-   **Club Notification System**: Sends alerts via **Twilio SMS** and personalized **emails** to a list of subscribed Flight Club members.
-   **Indirect Flight Search**: If no direct flights are found, the application automatically searches for cheaper routes with stopovers to find the best possible deal.
-   **Dynamic Member Management**: Manages both flight destinations and a user email list from separate tabs in a Google Sheet.
-   **Automated Data Enrichment**: Automatically finds and populates missing IATA airport codes for your destination cities.
-   **Secure Configuration**: All API keys and sensitive credentials are kept secure using a `.env` file.
-   **Modular Codebase**: The project is structured into logical classes for data management, flight searching, and notifications, making it easy to maintain and extend.

---

## ⚙️ How It Works

**Flight Club** executes a sophisticated workflow to find and report the best flight deals:

1.  **Fetch Club Data**: It connects to Google Sheets via the Sheety API to retrieve two sets of data:
    -   A list of cities and target prices from the 'Prices' sheet.
    -   A list of club members (first name, last name, email) from the 'Users' sheet.
2.  **Update IATA Codes**: It checks the 'Prices' sheet for any cities missing an IATA airport code, fetches it using the Amadeus API, and updates the sheet.
3.  **Search for Flights**: For each destination, the script performs a two-step search:
    -   First, it queries the Amadeus API for the cheapest **direct (non-stop)** flight.
    -   If no direct flight is found, it automatically performs a second search for **indirect flights** (with one or more stops).
4.  **Alert the Club**: If a flight's price is below the target price:
    -   An **SMS alert** is sent via Twilio with the core deal details.
    -   A **personalized email**, signed "Yours Sincerely, Flight Club," is sent to every member in the 'Users' list with detailed flight information.

---

## 🛠️ Technology Stack

-   **Language**: Python 3
-   **APIs**:
    -   **Amadeus**: For comprehensive flight data, including stopover information.
    -   **Sheety**: To read from and write to Google Sheets.
    -   **Twilio**: For sending SMS notifications.
-   **Core Libraries**:
    -   `requests`: For handling all API requests.
    -   `python-dotenv`: To manage environment variables.
    -   `smtplib`: For sending emails via a Gmail SMTP server.
      
---

## 🚀 Getting Started

Follow these instructions to get the project running locally.

### Prerequisites

-   Python 3.x installed.
-   Active accounts with [Amadeus for Developers](https://developers.amadeus.com/), [Sheety](https://sheety.co/), and [Twilio](https://www.twilio.com/).
-   A Google Account with an app password for sending emails.
-   A Google Sheet with two tabs:
    -   `prices`: with columns `city`, `iataCode`, and `lowestPrice`.
    -   `users`: with columns `firstName`, `lastName`, and `email`.

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: Create a `requirements.txt` file with `requests`, `python-dotenv`, and `twilio`.)*

4.  **Configure environment variables:**
    Create a `.env` file in the root directory and populate it with your credentials:

    ```env
    # Amadeus API Credentials
    AMADEUS_API_KEY="YOUR_AMADEUS_API_KEY"
    API_SECRET="YOUR_AMADEUS_API_SECRET"
    TOKEN_ENDPOINT="[https://test.api.amadeus.com/v1/security/oauth2/token](https://test.api.amadeus.com/v1/security/oauth2/token)"
    CITY_SEARCH_ENDPOINT="[https://test.api.amadeus.com/v1/reference-data/locations](https://test.api.amadeus.com/v1/reference-data/locations)"
    FLIGHT_ENDPOINT="[https://test.api.amadeus.com/v2/shopping/flight-offers](https://test.api.amadeus.com/v2/shopping/flight-offers)"
    ORIGIN_CITY_IATA="HYD" # Example: Hyderabad

    # Sheety API Endpoints
    SHEETY_PRICES_ENDPOINT="YOUR_SHEETY_PRICES_API_ENDPOINT"
    SHEETY_USERS_ENDPOINT="YOUR_SHEETY_USERS_API_ENDPOINT"
    SHEETY_USERNAME="YOUR_SHEETY_USERNAME"
    SHEETY_PASSWORD="YOUR_SHEETY_PASSWORD"

    # Twilio API Credentials
    TWILIO_SID="YOUR_TWILIO_ACCOUNT_SID"
    TWILIO_AUTH_TOKEN="YOUR_TWILIO_AUTH_TOKEN"
    TWILIO_VIRTUAL_NUMBER="YOUR_TWILIO_PHONE_NUMBER"
    TWilio_VERIFIED_NUMBER="YOUR_PERSONAL_PHONE_NUMBER"

    # Email Credentials (use a Google App Password)
    MY_MAIL="your-email@gmail.com"
    MY_PASS="your-google-app-password"
    ```

### Usage

To run the flight tracker, execute the main script from your terminal:

```bash
python main.py
```
---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
