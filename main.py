import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
# como quiero descargar las imagenes y manipular las rutas de archivos y directorios:
import os
from urllib.parse import urlparse

url = 'https://www.noticiasformosa.com.ar/'

def get_all_images(url): # obtener todas las imagenes de la url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = []
    for img in soup.findAll('img'):
        images.append(img.get('src'))
    return images

def download_images(images): # descargar todas las imagenes
    domain = urlparse(url).netloc
    if not os.path.exists(domain):
        os.mkdir(domain)
    for i, img in enumerate(images):
        try:
            response = requests.get(img)
            with open(os.path.join(domain, f'img_{i}.png'), 'wb') as f:
                f.write(response.content)
        except RequestException as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    print('Iniciadno extracción de imágenes... aguarde un momento')
    images = get_all_images(url)
    download_images(images)
    print('Extracción de imágenes finalizada, puede ver las imágenes en la carpeta correspondiente a la página')

# Ejecutar el script
# python main.py