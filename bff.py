from functools import wraps
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_GATEWAY_URL = 'http://localhost:2001/api'

def token_valid(token):
    headers = {'Authorization': f'Bearer {token}'}  # Bearerトークンを使用するように変更
    response = requests.get(f'{API_GATEWAY_URL}/validate_token', headers=headers)
    return response.status_code == 200

def token_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or not token.startswith('Bearer '):  # Bearerトークンかどうかを確認
            return jsonify({'message': 'Unauthorized'}), 401
        token = token.split(' ')[1]  # Bearerトークンからトークン部分を取り出す
        if token_valid(token):
            return func(*args, **kwargs)
        else:
            return jsonify({'message': 'Invalid token'}), 401
    return decorated_function

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
@token_required
def get_resource():
    token = request.headers.get('Authorization').split(' ')[1]  # Bearerトークンからトークン部分を取り出す
    response = requests.get(f'{API_GATEWAY_URL}/resource', headers={'Authorization': f'Bearer {token}'})  # Bearerトークンを使用するように変更
    return response.content, response.status_code

if __name__ == '__main__':
    app.run(debug=True, port=2000)
