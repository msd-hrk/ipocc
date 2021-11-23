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

@app.route('/listedCompanies')
def listedCompanys():
    """
    上場済み全データのうち指定日日数分のデータに整形して返却
    
    return
    ------
    flask:5000/listedCompanys?day=25 → 25日分
    day:default=30
    """
    day_count = request.args.get('day', default=30, type=int)

    data = wrap_contents(lc.get_listed_companies(day_count))
    return jsonify(data)

@app.route('/getDetail')
def getDetail():
    """
    上場済み全データから引数証券会社に該当するデータを返す
    
    return
    ------
    flask:5000/getDetail?securitiesNo=9999 
    """
    securities_no = str(request.args.get('securitiesNo', type=int))

    data = wrap_contents(lc.get_listed_companies(securities_no))
    return jsonify(data)



def wrap_contents(data):
        response = {
            "contents": data
        }
        return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
