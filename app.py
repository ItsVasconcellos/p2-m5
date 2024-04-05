# Módulos necessários para o funcionamento do código
from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from tinydb import TinyDB
from datetime import datetime 

app = Flask(__name__)
db = TinyDB('db.json')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ping')
def index():
    return jsonify({"resposta":"pong"})


@app.route('/ping', methods=['POST'])
def index():
    text = request.form['dados']
    return jsonify({"resposta":text})