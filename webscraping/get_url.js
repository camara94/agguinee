let urls = document.querySelectorAll("a.ZZ7G7b");
let categories = []
for(let i=0; i < urls.length; i++) {
    categories.push(urls[i].href);
}
let contenu = "";
for(let i=0; i < categories.length; i++) {
    contenu += categories[i] + "<==>"
}

let nomFichier = "";
nomFichier = document.querySelector("input.og3lId").value
nomFichier = document.querySelector("input.og3lId").value.replaceAll(" ", "_");

let telecharger = (contenu, nomFicher, contentType) => {

    const a = document.createElement("a");
    const fichier = new Blob([contenu], {type: contentType});
    a.href = URL.createObjectURL(fichier);
    a.download = nomFichier;
    a.click();
}
let lancerTelechargement = () => telecharger(contenu, nomFichier+".txt", "text/plain")
lancerTelechargement()   