# backend/app.py
from flask import Flask, jsonify
import random
from data_generator import generate_interface_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/data')
def get_data():
    # Generate random data for O-RAN interfaces
    data = generate_interface_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000)
