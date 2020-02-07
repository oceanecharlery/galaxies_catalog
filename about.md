# Catalogue de galaxies
Groupe composé de Océane Charlery, Sereyvuth Chum et Emilie Daongam. Projet de catalogue scientifique sous forme d'API composé d'une centaine d'objets extra galactiques.

## Données

### Propriétés de l'objet

#### Informations générales
- id (qui permet de faire le lien entre le numéro dans le catalogue de Messier et le numéro dans le catalogue NGC du même objet)
- code (numéro dans le catalogue)
- nom
- type (nébuleuse, amas, galaxie...)
- sous-type (Amas ouverts, Amas globulaires, Galaxies spirales, Galaxies lenticulaires, Galaxies elliptiques, Galaxies régulières, Nébuleuses planétaires, Nébuleuses diffuses, Vestiges de Supernova)
- constellation
- courbe de rotation (si galaxie spirale)
- image

___
#### Données sur la découverte
- astronome
- date
___
#### Données d’observation
- magnitude
- coordonnées galactiques (pour les nébuleuses)
- dimensions apparentes (pour les amas)
- dimensions (arcmin)
___
#### Données d’astrométrie
- Distance
___
Indiquer la complétude des données

## Intérêt scientifique
Mettre à disposition un vaste catalogue scientifique sur le ciel profond croisant plusieurs sources de données.

Sources : 
- Catalogue de Messier
- Centre de Données astronomiques de Strasbourg
- NGC
- SIMBAD


## Fonctionnalités

### Minimales
- Minimaliste : peu de méthodes 
- Documentation : informations sur tous les différents types d'appels

### Idéales
- Testable : l'API a un moyen trivial de tester les conditions d'erreur comme les erreurs de réseau ou les mauvaises données
- Stateless 
- Timebound : imposer une limite de temps sur chaque appel d'API pour garantir de bonnes performances


## Technologies




# Réponse d'un GET sur Insomnia : localhost/galaxies/messier/M42
Dans un exemple d'objet json récupéré avec Insomnia: localhost/galaxies messier/M42
{
  "data": [
    {
      "constellation": "Ori",
      "constellation_en": "Orion, Hunter",
      "constellation_fr": "Orion",
      "constellation_latin": "Orion",
      "declinaison": "-05:23:22.8",
      "discoverer": "Peiresc",
      "distance": "1500",
      "image_url_1": "http://www.lasam.ca/messier/M042.JPG",
      "image_url_2": "https://www.datastro.eu/api/v2/catalog/datasets/catalogue-de-messier/files/90397cbe3746fedbf7f3fe98dd95c2f2",
      "magnitude": "4",
      "messier": "M42",
      "ngc": "NGC 9176",
      "object_type": "Emission Nebula / Nébuleuse à émission",
      "right_ascension": "05:35:16.48",
      "season": "Winter / Hiver",
      "size": "30,0'",
      "year": "1610"
    }
  ]
}

On a la possibilité d'identifier les catégories importantes.
A partir de cela, j'ai créé les routes.
Pour cela on a choisi :
- constellation (category)
- constellation_en (category)
- constellation_fr (category)
- constellation_latin (category)
- discover (category)
- messier (id)
- ngc (category)
- object_type (category)
- season (category)