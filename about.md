# Catalogue de galaxies
Groupe composé de Océane Charlery, Sereyvuth Chum et Emilie Daongam. Projet de catalogue scientifique composé d'une centaine d'objets extra galactiques.

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