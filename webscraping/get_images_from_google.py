import argparse


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
