from flask import Flask, jsonify, request
import secrets

app = Flask(__name__)

# ユーザーの認証情報を仮の辞書で管理
users = {
    'user1': 'password1',
    'user2': 'password2'
}

# ユーザーごとにトークンを管理する辞書
tokens = {}

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username in users and users[username] == password:
        token = secrets.token_hex(16)
        tokens[token] = username
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/api/resource')
def get_resource():
    token = request.headers.get('Authorization')
    if token and token in tokens:
        username = tokens[token]
        return jsonify({'message': f'This is the resource for {username}'}), 200
    else:
        return jsonify({'message': 'Unauthorized'}), 401

if __name__ == '__main__':
    app.run(debug=True, port=2001)
