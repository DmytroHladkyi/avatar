import requests
import random
from pathlib import Path

response = requests.get(f'https://avatars.dicebear.com/api/micah/{random.random()}.svg')

Path('./avatars').mkdir(exist_ok=True) # stwarza się plik, gdzie będą przechowywać się pliki z linii (with open)
with open ('./avatars/avatara.svg', 'wb') as file: #/avatars/avatar.svg ---zapisujemy i KATALOG i NAZWE PLIKU
 file.write(response.content)