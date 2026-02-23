import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Déposez votre code à partir d'ici :
@app.route("/contact")
def MaPremiereAPI():
    return render_template("contact.html")

@app.get("/paris")
def api_paris():
    
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()

    times = data.get("hourly", {}).get("time", [])
    temps = data.get("hourly", {}).get("temperature_2m", [])

    n = min(len(times), len(temps))
    result = [
        {"datetime": times[i], "temperature_c": temps[i]}
        for i in range(n)
    ]

    return jsonify(result)

@app.route("/rapport")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme")
def monhistogramme():
    return render_template("histogramme.html")

# API pour récupérer les données de précipitations à Amsterdam
@app.get("/api-atelier")
def api_atelier():
    # URL générée sur open-meteo pour Amsterdam (précipitations)
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.3676&longitude=4.9041&hourly=precipitation"
    response = requests.get(url)
    data = response.json()

    times = data.get("hourly", {}).get("time", [])
    precipitations = data.get("hourly", {}).get("precipitation", [])

    n = min(len(times), len(precipitations))
    result = [
        {"datetime": times[i], "valeur": precipitations[i]}
        for i in range(n)
    ]

    return jsonify(result)

# Route pour afficher la page web de l'atelier
@app.route("/atelier")
def monatelier():
    return render_template("atelier.html")


# Ne rien mettre après ce commentaire
    
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
