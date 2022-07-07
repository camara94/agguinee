import argparse

from tqdm import tqdm
from bs4 import BeautifulSoup
from time import sleep
import requests


app = argparse.ArgumentParser()
app.add_argument("-l", "--lien", required=True,
                 help="Nous permet de spécifier le chemin du fichier d'url pour le webscraping")
app.add_argument("-s", "--startIndex", required=False,
                 help="Nous permet de spécifier l'indice de la première url à scraper")
app.add_argument("-e", "--endIndex", required=False,
                 help="Nous permet de spécifier l'indice de la dernière url à scraper")

args = vars(app.parse_args())

fichier = args["lien"]

texte = ""

with open(fichier, "r") as f:
    texte += f.readline()

urls = [url for url in texte.split("<==>")]


print(len(urls))
urlsFinal = []
if args["startIndex"] != None and args["endIndex"] != None:
    startIndex = int(args["startIndex"])
    endIndex = int(args["endIndex"])
    urlsFinal = urls[startIndex: endIndex]
elif args["startIndex"] != None and args["endIndex"] == None:
    startIndex = int(args["startIndex"])
    urlsFinal = urls[startIndex:]
elif args["startIndex"] == None and args["endIndex"] != None:
    endIndex = int(args["endIndex"])
    urlsFinal = urls[: endIndex]
elif args["startIndex"] == None and args["endIndex"] == None:
    urlsFinal = urls


def get_url_images_from_google(urls):
    url_images = []

    for url in tqdm(urls):
        print('TELECHARGEMENT ENCOURS.....')

        requete = requests.get(url)

        if requete.status_code != 200:
            print(f'Un problème est sur {url}')
        else:
            doc = BeautifulSoup(requete.content, "html.parser")
            for item in doc.find_all("img"):
                try:
                    url_images.append(item['src'])
                except:
                    pass
            sleep(8)

    return url_images


url_images = get_url_images_from_google(urlsFinal)
print(url_images)
