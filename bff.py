from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_GATEWAY_URL = 'http://localhost:2001/api'

@app.route('/bff/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    response = requests.post(f'{API_GATEWAY_URL}/login', json={'username': username, 'password': password})
    if response.status_code == 200:
        token = response.json().get('token')
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/bff/resource')
def get_resource():
    token = request.headers.get('Authorization')
    if token:
        response = requests.get(f'{API_GATEWAY_URL}/resource', headers={'Authorization': token})
        return response.content, response.status_code
    else:
        return jsonify({'message': 'Unauthorized'}), 401

if __name__ == '__main__':
    app.run(debug=True, port=2000)
