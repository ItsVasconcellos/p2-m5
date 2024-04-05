# Módulos necessários para o funcionamento do código
from flask import Flask, render_template, request, redirect, jsonify
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
def ping():
    db.insert({'data': str(datetime.now()), 'mensagem': 'ping'})
    return jsonify({"resposta":"pong"})


@app.route('/echo', methods=['POST'])
def echo():
    db.insert({'data': str(datetime.now()), 'mensagem': 'echo'})
    text = request.json
    text = text['dados']
    return jsonify({"resposta":text})

@app.route('/dash')
def dash():
    return render_template('dash.html')

@app.route('/info')
def info():
    data = db.all()
    return render_template('info.html', logs = data)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)