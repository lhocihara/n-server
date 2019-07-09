from flask import Flask, jsonify, request

app = Flask(__name__)
##Definição do endpoint
@app.route("/hi")
def mensagem de boas vindas():
    return "eae meu!!"