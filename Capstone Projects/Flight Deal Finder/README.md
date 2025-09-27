# ✈️ Flight Deal Finder & Notifier

This project automates the process of searching for the cheapest flights to your dream destinations. It uses a Google Sheet to manage your destination list and sends you an SMS alert via Twilio when a flight price drops below your target.



## ✨ Features

- **Dynamic Destination Management**: Easily add or remove destinations and target prices directly in a Google Sheet.
- **Automated IATA Code Lookup**: Automatically finds and populates missing IATA airport codes for your destination cities.
- **Real-time Flight Search**: Leverages the Amadeus API to find the cheapest flight prices within a given date range.
- **Instant SMS Alerts**: Get immediate notifications on your phone when a deal is found, powered by the Twilio API.
- **Secure & Configurable**: Keeps all your API keys and sensitive information secure using environment variables.

---

## ⚙️ How It Works

The script follows a simple, automated workflow:

1.  **Fetch Data from Google Sheets**: The application starts by connecting to your Google Sheet via the Sheety API to retrieve the list of cities you want to track and their corresponding target prices.
2.  **Enrich Destination Data**: It checks if any city in your sheet is missing its IATA airport code. If so, it queries the Amadeus API to find the correct code and updates your Google Sheet automatically.
3.  **Search for Flights**: For each destination, the script queries the Amadeus Flight Offers Search API to find the cheapest available flight from your specified origin city.
4.  **Compare & Notify**: If the price of a found flight is lower than your target price for that destination, the script will use the Twilio API to send you a formatted SMS message with all the deal details. If no deal is found, it simply logs the current price and moves on.

---

## 🛠️ Technology Stack

- **Language**: Python 3
- **APIs**:
    - **Amadeus**: For flight data and IATA code lookups.
    - **Sheety**: To read from and write to the Google Sheet.
    - **Twilio**: For sending SMS notifications.
- **Core Libraries**:
    - `requests`: To handle API requests.
    - `python-dotenv`: To manage environment variables.

---

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

- Python 3.x installed.
- Accounts with [Amadeus for Developers](https://developers.amadeus.com/), [Sheety](https://sheety.co/), and [Twilio](https://www.twilio.com/).
- A Google Sheet with the following columns: `city`, `iataCode`, and `lowestPrice`.

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Create a virtual environment and activate it:**
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
    *(Note: You'll need to create a `requirements.txt` file containing `requests`, `python-dotenv`, etc.)*

4.  **Set up your environment variables:**
    Create a file named `.env` in the root directory and add the following, replacing the placeholder values with your actual credentials:

    ```env
    # Amadeus API Credentials
    AMADEUS_API_KEY="YOUR_AMADEUS_API_KEY"
    API_SECRET="YOUR_AMADEUS_API_SECRET"
    TOKEN_ENDPOINT="[https://test.api.amadeus.com/v1/security/oauth2/token](https://test.api.amadeus.com/v1/security/oauth2/token)"
    CITY_SEARCH_ENDPOINT="[https://test.api.amadeus.com/v1/reference-data/locations](https://test.api.amadeus.com/v1/reference-data/locations)"
    FLIGHT_ENDPOINT="[https://test.api.amadeus.com/v2/shopping/flight-offers](https://test.api.amadeus.com/v2/shopping/flight-offers)"
    ORIGIN_CITY_IATA="LON" # Example: London

    # Sheety API Credentials
    SHEETY_ENDPOINT="YOUR_SHEETY_API_ENDPOINT"
    SHEETY_USERNAME="YOUR_SHEETY_USERNAME"
    SHEETY_PASSWORD="YOUR_SHEETY_PASSWORD"

    # Twilio API Credentials
    TWILIO_SID="YOUR_TWILIO_ACCOUNT_SID"
    TWILIO_AUTH_TOKEN="YOUR_TWILIO_AUTH_TOKEN"
    TWILIO_VIRTUAL_NUMBER="YOUR_TWILIO_PHONE_NUMBER"
    TWILIO_VERIFIED_NUMBER="YOUR_PERSONAL_PHONE_NUMBER"
    ```

### Usage

Once the setup is complete, simply run the main script from your terminal:

```bash
python main.py
```

The script will execute the flight search and send alerts if any deals are found. You can schedule this script to run periodically using cron jobs (Linux/macOS) or Task Scheduler (Windows) to keep monitoring prices automatically.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
