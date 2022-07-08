import argparse

from tqdm import tqdm
from bs4 import BeautifulSoup
from time import sleep
import requests

import os
import urllib

app = argparse.ArgumentParser()
app.add_argument("-d", "--dossier", required=True,
                 help="Nous permet de spécifier le chemin des fichiers d'url pour le webscraping")
app.add_argument("-s", "--startIndex", required=False,
                 help="Nous permet de spécifier l'indice de la première url à scraper")
app.add_argument("-e", "--endIndex", required=False,
                 help="Nous permet de spécifier l'indice de la dernière url à scraper")

args = vars(app.parse_args())

dossier = args["dossier"]


def fichier(fic):
    texte = ""
    nomFichier = fic[: fic.find(".txt")]
    with open(fic, "r") as f:
        texte += f.readline()

    urls = [url for url in texte.split("<==>")]

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

    return (nomFichier, urlsFinal)


def get_url_images_from_google(urls):
    url_images = []

    for url in tqdm(urls):
        print('TELECHARGEMENT ENCOURS.....')

        try:
            requete = requests.get(url)
        except:
            pass

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

    return url_images[1:]


def download_image_from_google(url_image, nomFichier, num=0):
    if os.path.exists(os.path.join("images/", nomFichier)):
        pass
    else:
        os.makedirs(os.path.join("images/", nomFichier))

    for index, url in tqdm(enumerate(url_image)):
        try:
            nomComplet = "images/" + nomFichier + "/" + str(index+1) + ".jpg"
            urllib.request.urlretrieve(url, nomComplet)
        except:
            pass
    print("Fin de téléchargement ....")


liste_fichier = os.listdir(dossier)

print("NOUS AVONS: ", liste_fichier, " FICHIERS")

for fic in tqdm(liste_fichier):
    fichier_urls = fichier(os.path.join("urls/", fic))
    url_images = get_url_images_from_google(fichier_urls[1])
    nomFichier = fic[:fic.find(".txt")]
    download_image_from_google(url_images, nomFichier)
