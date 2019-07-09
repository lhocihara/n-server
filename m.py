from flask import Flask, jsonify, request

app = Flask(__name__)
##Definição do endpoint
@app.route("/hi")
def boas_vindas():
    return jsonify({"message": "eae meu!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)