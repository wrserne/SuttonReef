from flask import Flask, request, render_template, jsonify, session
import psycopg2
from boggle import Boggle
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "fdfgkjtjkkg45yfdb"

db_connection = psycopg2.connect(
    database="test", user="postgres", password="secret")

url = "https://reef-pi.github.io/api/tcs/{id}/current_reading"
response = requests.get(url)

print(response.status_code)
print(response.json())


@app.route("/temperature", method=["GET"])
def temperature(reading):


    return render_template("index.html", url=url, response=response)


@app.route("/PH", method=["GET"])
def ph_reading():
    return jsonify(data)
