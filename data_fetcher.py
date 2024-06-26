import requests


def fetch_animal_data(animal_name):
    """Fetches animal data from the Ninja API"""
    API_KEY = "gTbcY2BwGi1Gj/oarE+aWg==FWIsZ8CbNm9KwGQN"
    BASE_URL = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {'X-Api-Key': API_KEY}

    response = requests.get(BASE_URL, headers=headers)
    animals_data = response.json()
    return animals_data
