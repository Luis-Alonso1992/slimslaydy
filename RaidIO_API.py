import requests
import os

from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("api_key")

def get_character_information():
    url = "https://raider.io/api/v1/characters/profile"

    params = {
        "access_key": api_key,
        "region": "us",
        "realm": "Thunderlord",
        "name": "SlimSlaydy",
        "fields": "gear,mythic_plus_scores_by_season:current"
    }

    response = requests.get(url, params=params)
    print("Status code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        season = data.get("mythic_plus_scores_by_season", [])
        current_season = season[0]
        scores = current_season.get("scores", {})
        return {
            "name": data.get("name"),
            "realm": data.get("realm"),
            "race": data.get("race"),
            "class": data.get("class"),
            "mythic_score": scores.get("all")
        }
    else:
        print("Request Failed")
        print(response.text[:500])


get_character_information()

