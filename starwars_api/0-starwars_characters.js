#!/usr/bin/node
// Récupère les arguments passés à partir de la ligne de commande
const argv = process.argv;
// URL de base pour accéder à l'API des films de Star Wars
const urlFilm = "https://swapi-api.hbtn.io/api/films/";
// Construit l'URL pour un film spécifique en utilisant l'ID passé comme argume
const urlMovie = `${urlFilm}${argv[2]}/`;

// Importe le module "request" pour faire des requêtes HTTP
const request = require("request");

// Effectue une requête HTTP GET pour obtenir les données du film
request(urlMovie, function (error, response, body) {
  // Vérifie s'il n'y a pas d'erreur dans la requête
  if (error == null) {
    // Parse le corps de la réponse pour obtenir un objet JavaScript
    const fbody = JSON.parse(body);
    // Récupère la liste des URL des personnages du film
    const characters = fbody.characters;

    // Vérifie si la liste des personnages existe et en contient au moins un
    if (characters && characters.length > 0) {
      // Définit la limite comme le nombre total de personnages
      const limit = characters.length;
      // Appelle la fonction CharRequest pour traiter le premier personnage
      CharRequest(0, characters[0], characters, limit);
    }
  } else {
    // Log toute erreur rencontrée lors de la requête du film
    console.log(error);
  }
});

// Fonction récursive pour traiter chaque URL de personnage
function CharRequest(idx, url, characters, limit) {
  // Vérifie si tous les personnages ont été traités
  if (idx === limit) {
    return;
  }
  // Effectue une requête HTTP GET pour obtenir les données du personnage
  request(url, function (error, response, body) {
    // Vérifie s'il n'y a pas d'erreur dans la requête
    if (!error) {
      // Parse le corps de la réponse pour obtenir un objet JavaScript
      const rbody = JSON.parse(body);
      // Affiche le nom du personnage
      console.log(rbody.name);
      // Incrémente l'index et passe au personnage suivant
      idx++;
      CharRequest(idx, characters[idx], characters, limit);
    } else {
      // Log toute erreur rencontrée lors de la requête du personnage
      console.error("error:", error);
    }
  });
}
