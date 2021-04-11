import requests
import json
import pprint
from tqdm import tqdm


for current_page in tqdm(range(1, 334)):
    image_list = []

    response = requests.get(
        f"https://unsplash.com/napi/search/photos?query=indian "
        f"faces&per_page=30&page={current_page}")

    data = json.loads(response.content)['results']

    for obj in data:
        image_list.append(obj['urls']['small'] + "\n")

    with open('links.txt', 'a') as f:
        f.writelines(image_list)
