import requests
from urllib.parse import urlsplit
import os
import random
from tools import save_image
from dotenv import load_dotenv


def get_extension(image_link):
    extension = os.path.splitext(image_link[2])
    return extension[1]


def get_nasa_apod_images(nasa_api_key):
    min = 30
    max = 50
    count = random.randint(min, max)
    payload = {"api_key": nasa_api_key, "count" : count}
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for index, response in enumerate(response.json()):
        nasa_image_url = response['url']
        image_link = urlsplit(nasa_image_url)
        img_extension = get_extension(image_link)
        print(img_extension)
        filename = f'images/Nasa_apod_{index}{img_extension}'
        if img_extension != "":
            save_image(nasa_image_url, filename)


def main():
    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    get_nasa_apod_images(nasa_token)


if __name__ == "__main__":
    main()