# Machine Learning Engineer Training Project (Datascientest)
<br><br>
Le but de ce projet est de mettre en production un modèle d'analyse de sentiment construit sur le jeu de données de commentaires sur Disneyland: https://www.kaggle.com/arushchillar/disneyland-reviews 
<br><br>
## Travail demandé
###  L'API<br>
On va dans un premier construire une API avec Flask ou FastAPI. Cette API devra permettre d'interroger les différents modèles. Les utilisateurs pourront aussi interroger l'API pour accéder aux performances de l'algorithme sur les jeux de tests. Enfin il faut permettre aux utilisateurs d'utiliser une identification basique. (On pourra utiliser le header Authentication et encoder username:password en base 64). On pourra utiliser la liste d'utilisateurs/mots de passe suivante:

alice: wonderland
bob: builder
clementine: mandarine
...
<br><br>
### Le container<br>
Il s'agira ici de créer un container Docker pour déployer facilement l'API. On portera une attention particulière aux librairies Python à installer ainsi qu'à leurs différentes versions.
<br><br>
### Les tests<br>
Une série de tests devra être créée pour tester l'API contenairisée. On pourra pour cela créé un fichier docker-compose.yml en s'inspirant de ce qui a été fait dans l'évaluation de Docker.
<br><br>
### Kubernetes<br>
On pourra enfin créer un fichier de déploiement ainsi qu'un Service et un Ingress avec Kubernetes pour permettre le déploiement de l'API sur au moins 3 Pods.
<br><br>
## Présentation du Projet délivré<br>
Mon travaille est décrit ici
<br>
[version FR](https://github.com/damienld/MLE-Project/blob/main/Documentation%20MLE%20projet.pdf)<br>
[version EN](https://github.com/damienld/MLE-Project/blob/main/Documentation%20MLE%20projet_EN.pdf)<br>
Et l'API tourne [ici] (https://disneyreviews.azurewebsites.net/docs#/) (nécessite quelques minutes pour lancer le conteneur au premier appel)

