from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/hello')
def hello():

    client = MongoClient("mongodb+srv://flask:flask@cluster0.hrlio.mongodb.net/ipocc?retryWrites=true&w=majority")
    db = client.ipocc
    collection = db.codelist
    data = collection.find_one({'securitiesNo': '6227'})
    del data["_id"]
    print(data)
    return jsonify(data)

@app.route('/func')
def func():
    return 'welcome! func!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
