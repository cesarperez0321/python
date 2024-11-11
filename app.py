from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS en la aplicación

@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello World-Educare.ai")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
