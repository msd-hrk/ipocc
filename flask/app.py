from flask import Flask, jsonify, request
from pymongo import MongoClient
from page_method import hello as hllo
from page_method import listed_list as ll

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/hello')
def hello():
    """
    サンプルデータ取得用（１データ）
    
    return
    ------
    flask:5000/hello
    """
    data = hllo.getHello()
    return jsonify(data)

@app.route('/listedList')
def listed_list():
    """
    上場済み全データ取得して返す
    
    return
    ------
    flask:5000/listedList
    """
    data = ll.get_listed_list()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
