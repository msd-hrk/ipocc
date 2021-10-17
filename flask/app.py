from flask import Flask, jsonify, request
from pymongo import MongoClient
from page_method import hello as hllo
from page_method import listed_list as ll
from page_method import listed_companies as lc

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
    data = wrap_contents(ll.get_listed_list())
    return jsonify(data)

@app.route('/listedCompanies/<int:day_count>')
def listedCompanys(day_count):
    """
    上場済み全データのうち指定日日数分のデータに整形して返却
    
    return
    ------
    flask:5000/listedCompanys/30 → 30日分
    """
    data = wrap_contents(lc.get_listed_companies(day_count))
    return jsonify(data)

def wrap_contents(data):
        response = {
            "contents": data
        }
        return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
