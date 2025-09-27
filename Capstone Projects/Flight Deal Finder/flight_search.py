import requests

class FlightSearch:
    """
    Manages all interactions with the Amadeus API: OAuth token management, 
    city IATA code lookup, and flight offers search.
    """
    def __init__(self, api_key, api_secret, token_endpoint, city_endpoint, flight_endpoint):
        """
        Initializes with Amadeus endpoints and credentials. Obtains an access token immediately.
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.token_endpoint = token_endpoint
        self.city_endpoint = city_endpoint
        self.flight_endpoint = flight_endpoint
        
        self.access_token = self._get_new_token()
        self.headers = {"Authorization": f"Bearer {self.access_token}"}
        
    def _get_new_token(self):
        """Requests and returns a new Amadeus OAuth access token."""
        print("Acquiring new Amadeus access token...")
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        try:
            response = requests.post(url=self.token_endpoint, headers=header, data=body)
            response.raise_for_status()
            print("Token acquired successfully.")
            return response.json()['access_token']
        except requests.exceptions.RequestException as e:
            print(f"Error getting Amadeus token: {e}")
            return None

    def get_iata_code(self, city_name: str):
        """
        Searches for the 3-letter IATA code for a given city name.
        
        Returns:
            str or None: The IATA code if found, otherwise None.
        """
        city_params = {'keyword': city_name, 'max': '1'}
        print(f"Searching for IATA code for {city_name}...")
        try:
            response = requests.get(url=self.city_endpoint, params=city_params, headers=self.headers)
            response.raise_for_status()
            data = response.json().get('data', [])
            if data and 'iataCode' in data[0]:
                return data[0]['iataCode']
            else:
                print(f"Could not find IATA code for {city_name}.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error during City Search API call: {e}")
            return None

    def check_flights(self, origin_code, destination_code, departure_date, arrival_date):
        """
        Searches for the cheapest non-stop flight price for the given route and date.
        
        Returns:
            str or None: The 'grandTotal' price as a string, or None if no flight is found.
        """
        print(f'🔄 Getting Flight Details for {destination_code} from {origin_code}...')
        query = {
            "originLocationCode": origin_code,
            "destinationLocationCode": destination_code,
            "departureDate": departure_date,
            "returnDate":arrival_date,
            "adults": 1,
            "currencyCode": "GBP",
            "max": "1",
            "nonStop": "true"
        }
        try:
            response = requests.get(url=self.flight_endpoint, headers=self.headers, params=query)
            response.raise_for_status()
            result = response.json()
            
            if result.get('data') and len(result['data']) > 0:
                total_price = result['data'][0]['price']['grandTotal']
                return total_price
            else:
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error during Flight Offers API call: {e}")
            return None
