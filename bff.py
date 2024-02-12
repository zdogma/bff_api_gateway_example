from flask import Flask, jsonify, request, redirect
import requests

app = Flask(__name__)

API_GATEWAY_URL = 'http://localhost:2001/api'

@app.route('/bff/resource')
def get_bff_resource():
    api_response = requests.get(f'{API_GATEWAY_URL}/resource')
    return api_response.content, api_response.status_code

if __name__ == '__main__':
    app.run(debug=True, port=2000)