import requests
from pathlib import Path
from urllib.parse import urlsplit
import os
import random


def extension(image_link):
    extension = os.path.splitext(image_link[2])
    return extension[1]


def save_images(url, filename, api_key=""):
    payload = {"api_key" : api_key}
    Path("images").mkdir(parents=True, exist_ok=True)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    response.raise_for_status()
    for index, image in enumerate(
        response.json()['links']['flickr']['original']):
            filename = f"images/spaceX_{index}.jpg"
            save_images(image, filename)


def get_nasa_apod_images(nasa_api_key):
    count = random.randint(30, 50)
    payload = {"api_key": nasa_api_key, "count" : count}
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for index, response in enumerate(response.json()):
        nasa_image_url = response['url']
        image_link = urlsplit(nasa_image_url)
        img_extension = extension(image_link)
        filename = f'images/Nasa_apod_{index}{img_extension}'
        save_images(nasa_image_url, filename)

def get_nasa_planet_image(nasa_api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    count = random.randint(5, 10)
    payload = {"api_key" : nasa_api_key}
    for index in range(count):
        response = requests.get(url, params=payload)
        response.raise_for_status()
        epic_response = response.json()[index]
        epic_image_name = epic_response["image"]
        epic_image_date = epic_response["date"]
        splited_day = epic_image_date.split()
        splited_date = splited_day[0].split("-")
        epic_url =         f"https://api.nasa.gov/EPIC/archive/natural/{splited_date[0]}/{splited_date[1]}/{splited_date[2]}/png/{epic_image_name}.png"
        filename = f"images/nasa_planet_image_{index}.png"
        save_images(epic_url, filename, nasa_api_key)


def main():
    nasa_api_key = "0rIv85cpecbP541zZfUgJFSrU9dbpVjkOC0xgsTS"
    #get_nasa_apod_images(nasa_api_key)
    #fetch_spacex_last_launch()
    get_nasa_planet_image(nasa_api_key)


if __name__ == "__main__":
    main()