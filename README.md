# TP Docker

Ce projet contient un container avec une application Flask simple qui affiche une page de bienvenue. Elle est prête à être déployée en utilisant Docker.Le but de se projet est de découvrir l'outils Docker :
* Démarrer un container Docker avec une image de hub.docker.com.
* Construire un container Docker avec une application personnalisée en utilisant le fichier Dockerfile.
* Lancer plusieurs containers Docker en utilisant docker-compose
    * Dans ce TP nous avons créer un docker compose avec : 
        * L'application Flask
        * Prometheus (avec l'application Flask en target)
        * Grafana

-----------------------------------

## Prérequis

- Git (Instalation de git : https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)
- Docker (Installation de git sur Ubuntu : https://docs.docker.com/engine/install/ubuntu/)

-----------------------------------

## Étapes pour exécuter un container docker Flask via une image de hub.docker.com

#### 1. Lancer le container
```
sudo docker run -p 127.0.0.1:8000:8000 flask:latest
```
Ici l'application sera accessible sur l'ip : 127.0.0.1 sur le port 8000.
http://127.0.0.1:8000

------------------------------------

## Construire un container Docker avec une application personnalisée en utilisant le fichier Dockerfile.

#### 1. Créer un fichier Dockerfile

Exemple de ffichier Dockerfile :

```
# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install flask==3.0.*
RUN pip install prometheus_flask_exporter 

# install app
COPY flask_docker.py /

# final configuration
ENV FLASK_APP=flask_docker
EXPOSE 8000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]
```

#### 2. Lancer le container configuré avec le Dockerfile

``` 
docker build -t flasktest:latest .
```

``` 
docker run -d -p 8000:8000 flasktest
```

## Construire un Docker-Compose contenant plusieurs container.

#### 1. Cloner le repo git

```
git clone git@github.com:TomLebretonSupdevinci/TP1_Docker.git
```

#### 2. Build les applications avec docker-compose
Le fichier compose.yaml contient la configuration des 3 containers (Flask, Promotheus et Grafana)
Le fichier promotheus.yaml contient lui la configuration du scrapping de Promotheus afin de récupérer les targets et donc les metrics.

Commande pour lancer le build du docker compose :

```
docker-compose build
docker-compose up
```

Se connecter aux différentes applications : 
* Flask : http://127.0.0.1:8000
* Promotheus : http://127.0.0.1:9090
* Grafana : http://127.0.0.1:3000

Pour se connecter à Grafana, utiliser ces identifiants par défaut : 
Utilisateur : admin
Mot de passe : admin

Il vous est maintenant possible de créer une datasource  Prometheus dans Grafana pour visualiser vos données.
Ici la query utilisé est la suivante : 
``` sum(flask_http_request_total) by (status) ```



-----------------------------------

## Auteurs

- Boulen Pierre
- Lebreton Tom
