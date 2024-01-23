import requests
from urllib.parse import urlsplit
import os
import random
from tools import save_images


def get_extension(image_link):
    extension = os.path.splitext(image_link[2])
    return extension[1]


def get_nasa_apod_images(nasa_api_key):
    count = random.randint(30, 50)
    payload = {"api_key": nasa_api_key, "count" : count}
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for index, response in enumerate(response.json()):
        nasa_image_url = response['url']
        image_link = urlsplit(nasa_image_url)
        img_extension = get_extension(image_link)
        filename = f'images/Nasa_apod_{index}{img_extension}'
        save_images(nasa_image_url, filename)


def main():
    nasa_api_key = "0rIv85cpecbP541zZfUgJFSrU9dbpVjkOC0xgsTS"
    get_nasa_apod_images(nasa_api_key)


if __name__ == "__main__":
    main()