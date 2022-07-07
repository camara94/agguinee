import argparse


app = argparse.ArgumentParser()
app.add_argument("-l", "--lien", required=True,
                 help="Nous permet de spécifier le chemin du fichier d'url pour le webscraping")

args = vars(app.parse_args())

fichier = args["lien"]

texte = ""

with open(fichier, "r") as f:
    texte += f.readline()

urls = [url for url in texte.split("<==>")]

print(urls[0])
