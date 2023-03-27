import socket
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/product/<string:code>")
def product(code):
    response = requests.get(f"http://localhost:8000/products/{code}")
    if response.status_code == 200:
        return jsonify(response.json(), 200)
    elif response.status_code == 404:
        return jsonify(response.json(), 404)

if __name__ == '__main__':
    app.run(port=3000, debug=True)