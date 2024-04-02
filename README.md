# TP Docker

Ce projet contient une application Flask simple qui affiche une page de bienvenue. Elle est prête à être déployée en utilisant Docker.

## Prérequis

- Git
- Docker

## Étapes pour exécuter l'application

### 1. Cloner le dépôt

git clone git@github.com:TomLebretonSupdevinci/TP1_Docker.git

### 2. Construire l'image Docker

cd TP1_Docker
sudo docker run -p 127.0.0.1:8000:8000 flask:latest 

### 3. Lancer l'application

docker run -p 127.0.0.1:8000:8000 flask:latest

## Auteurs

- Boulen Pierre
- Lebreton Tom
