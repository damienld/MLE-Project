# MLE-Project
 Machine Learning Engineer Training Project (Datascientest)
 <br><br>
Le but de ce projet est de mettre en production un modèle d'analyse de sentiment construit sur le jeu de données de commentaires sur Disneyland: https://www.kaggle.com/arushchillar/disneyland-reviews 
<br><br>
L'API<br>
On va dans un premier construire une API avec Flask ou FastAPI. Cette API devra permettre d'interroger les différents modèles. Les utilisateurs pourront aussi interroger l'API pour accéder aux performances de l'algorithme sur les jeux de tests. Enfin il faut permettre aux utilisateurs d'utiliser une identification basique. (On pourra utiliser le header Authentication et encoder username:password en base 64). On pourra utiliser la liste d'utilisateurs/mots de passe suivante:

alice: wonderland
bob: builder
clementine: mandarine
...
<br><br>
Le container<br>
Il s'agira ici de créer un container Docker pour déployer facilement l'API. On portera une attention particulière aux librairies Python à installer ainsi qu'à leurs différentes versions.
<br><br>
Les tests<br>
Une série de tests devra être créée pour tester l'API contenairisée. On pourra pour cela créé un fichier docker-compose.yml en s'inspirant de ce qui a été fait dans l'évaluation de Docker.
<br><br>
Kubernetes<br>
On pourra enfin créer un fichier de déploiement ainsi qu'un Service et un Ingress avec Kubernetes pour permettre le déploiement de l'API sur au moins 3 Pods.
<br><br>
Rendus<br>
Les attendus sont un fichier pdf contenant des précisions sur les fichiers, sur les différentes étapes ainsi que sur les choix effectués. On devra aussi rendre un repo Github sur lequel seront les fichiers suivants:
fichier source de l'API
Dockerfile de l'API
dans un dossier l'ensemble des fichiers utilisés pour créer les tests
les fichiers de déploiements de Kubernetes
tout autre fichier ayant été utilisés pour faire ce projet.
