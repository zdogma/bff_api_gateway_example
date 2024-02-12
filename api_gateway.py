from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/resource')
def get_resource():
    # dummy
    data = {'message': 'This is the resource from the backend API'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=2001)