import requests
from pathlib import Path
import os


def save_image(url, filename, api_key=""):
    payload = {"api_key" : api_key}
    Path("images").mkdir(parents=True, exist_ok=True)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)