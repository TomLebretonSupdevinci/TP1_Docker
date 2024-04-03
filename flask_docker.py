from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)

@app.route("/")
def hello_world():
    return "<h1>Bienvenue sur la page d'accueil du TP Docker</h1> <p>Par Boulen Pierre et Lebreton Tom</p> <img src='https://c4.wallpaperflare.com/wallpaper/414/284/24/docker-containers-brand-wallpaper-preview.jpg'/>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)