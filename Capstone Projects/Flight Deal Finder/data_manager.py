import requests

class FlightDataManager:
    """
    Manages interaction with the Google Sheet (via Sheety API) for 
    reading destination data and updating IATA codes.
    """
    def __init__(self, endpoint, username, password):
        """
        Initializes the manager with Sheety credentials and endpoint.
        """
        self.endpoint = endpoint
        self.auth = (username, password)

    def get_destination_data(self):
        """
        Fetches all destination rows and target prices from the sheet.
        
        Returns:
            list: A list of dictionaries representing the sheet rows, or an empty list on failure.
        """
        print("Fetching destination data from Sheety...")
        try:
            response = requests.get(url=self.endpoint, auth=self.auth)
            response.raise_for_status()
            # Expects a JSON response like {'prices': [row1, row2, ...]}
            return response.json().get('prices', [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from Sheety: {e}")
            return []

    def update_iata_code(self, row_id: int, iata_code: str):
        """
        Updates a specific row in the sheet with the 3-letter IATA code.
        
        Args:
            row_id: The Sheety ID of the row to update.
            iata_code: The IATA code string to insert.
        """
        print(f"Updating IATA code for row {row_id} to {iata_code}...")
        sheety_updated_url = f"{self.endpoint}/{row_id}"
        body = {
            'price': {
                'iataCode': iata_code
            }
        }
        try:
            response = requests.put(
                url=sheety_updated_url,
                json=body,
                auth=self.auth
            )
            response.raise_for_status()
            print("IATA code updated successfully.")
        except requests.exceptions.RequestException as e:
            print(f"Error updating IATA code in Sheety: {e}")
