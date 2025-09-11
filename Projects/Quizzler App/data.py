import requests

response = requests.get(url=f"https://opentdb.com/api.php?amount=10&category=21&type=boolean")
response.raise_for_status()
question_data = response.json()['results']
