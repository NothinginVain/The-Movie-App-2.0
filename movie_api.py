import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')

URL = f'https://www.omdbapi.com/'


def fetch_movie_data(title):
    params = { 't': title, 'apikey': API_KEY}
    url = f'https://www.omdbapi.com/'
    try:
        result = requests.get(url, params=params, timeout=6)
        result.raise_for_status()
        return result.json()

    except requests.exceptions.RequestException as e:
        print('API request failed:', e)
        return None


