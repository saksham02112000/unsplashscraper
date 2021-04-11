from secrets import token_hex
from tqdm import tqdm
import requests

with open('links.txt', 'r') as f:
    image_list = f.readlines()
    for row in range(len(image_list)):
        image_list[row] = image_list[row].strip()

for image in tqdm(image_list[2500:3000]):
    r = requests.get(image, stream=True)

    with open("D:/images/" + token_hex(3) + ".jpg", 'wb') as f:

        for chunk in r.iter_content(chunk_size=1024 * 1024):

            if chunk:
                f.write(chunk)