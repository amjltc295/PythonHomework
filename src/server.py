from flask import Flask, request, jsonify
from flask_cors import CORS

from logging_config import logger


app = Flask(__name__)
CORS(app)

@app.route('/hi', methods=['GET'])
def hi():
    return jsonify(
        {"message": "Hi! This is the server for Introduction to Computer."})


if __name__ == "__main__":
    app.run()
