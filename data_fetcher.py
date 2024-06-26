import requests
import os
from dotenv import load_dotenv

load_dotenv()


def fetch_animal_data(animal_name):
    """Fetches animal data from the Ninja API"""
    API_KEY = os.getenv("API_KEY")
    BASE_URL = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {'X-Api-Key': API_KEY}

    response = requests.get(BASE_URL, headers=headers)
    animals_data = response.json()
    return animals_data
