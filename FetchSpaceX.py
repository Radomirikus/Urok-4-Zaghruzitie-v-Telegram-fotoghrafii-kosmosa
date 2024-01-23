import requests
from tools import save_images
import argparse


def fetch_spacex_last_launch(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    for index, image in enumerate(response.json()['links']['flickr']['original']):
            filename = f"images/spaceX_{index}.jpg"
            save_images(image, filename)


def main():
    parser = argparse.ArgumentParser(description='Скачивает изображения запуска ракет SpaceХ')
    parser.add_argument('--ID', help=('укажите айоди последнего запуска'), default="5eb87d47ffd86e000604b38a")
    args = parser.parse_args()
    fetch_spacex_last_launch(args.ID)


if __name__ == "__main__":
    main()