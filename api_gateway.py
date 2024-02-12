from flask import Flask, jsonify, request
import secrets

app = Flask(__name__)

# ユーザーの認証情報を仮の辞書で管理
users = {
    'user1': 'password1',
    'user2': 'password2'
}

# 一旦はメモリ上に残す
tokens = {}

def token_valid(token):
    return token in tokens

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username in users and users[username] == password:
        token = secrets.token_hex(16)
        tokens[token] = username
        return jsonify({'token': token, 'username': username}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/api/validate_token', methods=['GET'])
def validate_token():
    token = request.headers.get('Authorization')
    if token and token_valid(token):
        return jsonify({'message': 'Valid token'}), 200
    else:
        return jsonify({'message': 'Invalid token'}), 401

@app.route('/api/resource')
def get_resource():
    token = request.headers.get('Authorization')
    if token and token_valid(token):
        username = tokens[token]
        return jsonify({'message': f'This is the resource for {username}'}), 200
    else:
        return jsonify({'message': 'Unauthorized'}), 401

if __name__ == '__main__':
    app.run(debug=True, port=2001)
