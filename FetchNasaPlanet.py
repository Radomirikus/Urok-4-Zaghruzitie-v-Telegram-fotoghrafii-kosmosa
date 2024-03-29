import requests
import random
from tools import save_image
from dotenv import load_dotenv
import os



def get_nasa_planet_images(nasa_api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    min = 5
    max = 10
    count = random.randint(min, max)
    payload = {"api_key" : nasa_api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    response_result = response.json()

    for index in range(count):
        epic_response = response_result[index]
        epic_image_name = epic_response["image"]
        epic_image_date = epic_response["date"]
        splited_day = epic_image_date.split()
        splited_date = splited_day[0].split("-")
        epic_url = f"https://api.nasa.gov/EPIC/archive/natural/{splited_date[0]}/{splited_date[1]}/{splited_date[2]}/png/{epic_image_name}.png"
        filename = f"images/nasa_planet_image_{index}.png"
        save_image(epic_url, filename, nasa_api_key)


def main():
    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    get_nasa_planet_images(nasa_token)


if __name__ == "__main__":
    main()