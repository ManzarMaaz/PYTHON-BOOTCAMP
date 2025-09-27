# Standard Library Imports
import time
from datetime import date, timedelta
import os 
from dotenv import load_dotenv # Used to load the .env file

# Import modules (classes) from local files
from notification_manager import NotificationManager
from data_manager import FlightDataManager
from flight_search import FlightSearch
from flight_data import FlightData

# ==============================================================================
# 1. CONFIGURATION CONSTANTS
# ==============================================================================
# Load environment variables from .env file
load_dotenv()

# Amadeus Config
AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
API_SECRET = os.getenv("API_SECRET")
TOKEN_ENDPOINT = os.getenv("TOKEN_ENDPOINT")
CITY_SEARCH_ENDPOINT = os.getenv("CITY_SEARCH_ENDPOINT")
FLIGHT_ENDPOINT = os.getenv("FLIGHT_ENDPOINT")
ORIGIN_CITY_IATA = os.getenv("ORIGIN_CITY_IATA")

DEPARTURE_DATE = date.today() + timedelta(1)
ARRIVAL_DATE = DEPARTURE_DATE + timedelta(30)

# Sheety Config
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")

# Twilio Config
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.getenv("TWILIO_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.getenv("TWILIO_VERIFIED_NUMBER")

# ==============================================================================
# 2. MAIN ORCHESTRATION FUNCTION
# ==============================================================================
def run_flight_tracker():
    """Initializes managers and executes the core price checking loop."""
    
    # Initialize all services by passing environment variables to constructors
    data_manager = FlightDataManager(SHEETY_ENDPOINT, SHEETY_USERNAME, SHEETY_PASSWORD)
    flight_search = FlightSearch(
        AMADEUS_API_KEY, 
        API_SECRET, 
        TOKEN_ENDPOINT, 
        CITY_SEARCH_ENDPOINT, 
        FLIGHT_ENDPOINT
    )
    notification_manager = NotificationManager(
        TWILIO_SID, 
        TWILIO_AUTH_TOKEN, 
        TWILIO_VIRTUAL_NUMBER, 
        TWILIO_VERIFIED_NUMBER
    )
    
    # 1. Get destination data from Google Sheet
    sheet_data = data_manager.get_destination_data()

    if not sheet_data or not flight_search.access_token:
        print("Initialization failed (No data or no Amadeus token). Exiting.")
        return
    
    # Convert sheet data rows to FlightData objects
    flight_deals = [
        FlightData(
            city_name=row['city'],
            iata_code=row.get('iataCode', ''), # Use empty string if missing
            target_price=float(row['lowestPrice']),
            row_id=row['id']
        )
        for row in sheet_data
    ]

    # 2. Update IATA codes if missing in the sheet
    for deal in flight_deals:
        if not deal.iata_code:
            iata_code = flight_search.get_iata_code(deal.city_name)
            
            if iata_code:
                # Update Sheety via the manager
                data_manager.update_iata_code(deal.row_id, iata_code)
                # Update local object
                deal.iata_code = iata_code

    # 3. Search for flights and compare prices
    print("\n--- Starting Flight Search Loop ---\n")
    for deal in flight_deals:
        if not deal.iata_code:
            print(f"Skipping {deal.city_name}: Missing IATA code after lookup.")
            continue

        # Get the cheapest flight price
        cheapest_price_str = flight_search.check_flights(
            origin_code=ORIGIN_CITY_IATA,
            destination_code=deal.iata_code,
            departure_date=DEPARTURE_DATE,
            arrival_date = ARRIVAL_DATE
        )
        
        if cheapest_price_str is None:
            print(f"❌ No flight deals found for {deal.city_name}.\n")
            continue
            
        deal.cheapest_price = float(cheapest_price_str)
        
        print(f'✅ Found price £{deal.cheapest_price:.2f} for flight to {deal.city_name}. Target price is £{deal.target_price:.2f}.\n')
        
        # 4. Compare prices and send alert
        if deal.cheapest_price < deal.target_price:
            message = (
                f"🚨 Low Price Alert! Fly for only £{deal.cheapest_price:.2f} "
                f"to {deal.city_name} ({deal.iata_code}) from {ORIGIN_CITY_IATA} "
                f"on {DEPARTURE_DATE}."
            )
            notification_manager.send_sms(message)
        else:
            print(f"Price £{deal.cheapest_price:.2f} is higher than target £{deal.target_price:.2f}. No alert sent.\n")


if __name__ == "__main__":
    run_flight_tracker()
