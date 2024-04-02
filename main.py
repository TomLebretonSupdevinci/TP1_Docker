from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Bienvenue sur la page d'acceuil du TP Docker</h1> <p>Par Boulen Pierre et Lebreton Tom</p> <img src='https://c4.wallpaperflare.com/wallpaper/414/284/24/docker-containers-brand-wallpaper-preview.jpg'/>"