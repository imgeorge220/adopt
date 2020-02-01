from secrets import BEAR_KEY
import requests
import random


def get_animal():
    header = {"Authorization": f"Bearer {BEAR_KEY}"}
    resp = requests.get("https://api.petfinder.com/v2/animals",
                        headers=header)
    animals = resp.json()
    animal_full_data = random.choice(animals['animals'])
    print('**************', animal_full_data, '****************************')
    animal = {
        'name': animal_full_data.get("name"),
        'age': animal_full_data.get("age"),
    }
    
    return animal
