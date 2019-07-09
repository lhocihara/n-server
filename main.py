# -*- coding: utf-8 -*-
import os, pymongo, dns
from flask import Flask, jsonify, request
from flask_json_schema import JsonSchema, JsonValidationError

app = Flask(__name__)

#Setando tratamento de erros na validação
@app.errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify({ 'Erro': e.message, 'Errors': [validation_error.message for validation_error in e.errors]})

@app.route('/')
def nao_entre_em_panico():
    if request.headers.get('Authorization') == '42':
        return jsonify({"42": "Nao entra em panico, soh estou fazendo o tcc, e com autorização, hehe!"})
    return jsonify({"message": "Nao entra em panico, soh estou fazendo o tcc, utilizando o tcc!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)