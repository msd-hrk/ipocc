from flask import Flask, jsonify, request
from pymongo import MongoClient
from page_method import hello as hllo

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/hello')
def hello():
    data = hllo.getHello()
    return jsonify(data)

@app.route('/func')
def func():
    return 'welcome! func!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
