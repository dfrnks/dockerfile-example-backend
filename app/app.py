from flask import Flask, jsonify
from flask_cors import CORS
from random_word import RandomWords

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello world"


@app.route("/list")
def list():
    r = RandomWords()
    return jsonify(r.get_random_words())


if __name__ == "__main__":
    app.run(host='0.0.0.0')
