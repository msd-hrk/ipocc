from config import config
from datetime import timedelta
from pymongo import MongoClient
import datetime

class DbCommon():
    """
    mongoDB接続クラス

    Attributes
    ----------
    client : MongoClient
        mongoクライアント
    db : DB
        接続先DB
    collection : mongo collection
        取得コレクション
    """

    def __init__(self):
        """
        mongoDBクライアントを取得し、保持する
        """
        conf = config.Config()
        self.client = MongoClient(conf.mongo_url)
        self.db = self.client.ipocc
        self.collection = self.db.codelist
        
    def find_one_from_securities_no(self, securities_no):
        """
        securitiesNo(証券コード)から該当データを取得し返す

        parameters
        ----------
        securities_no : str
            証券コード
        
        returns
        -------
        mongo_data : dict
            mongoDBに登録されている該当データ
        """
        data = self.collection.find_one({"securitiesNo": securities_no}, {"_id": 0})
        return data
    
    def find_all_data(self):
        """
        mongoDBに保存されている全データを返す

        return
        ------
        data : dict
            登録済みデータすべてを返す
        """
        data = self.collection.find({}, {"_id": 0})
        return data
    
    def find_listed_data(self):
        """
        上場しているデータを返す

        return
        ------
        data : dict
            上場済みのデータを返す
        
        Notes
        -----
        メソッド起動時が22時を超えていない場合は
        起動日に上場するデータは除く
        priceDiaryフィールドがない（上場廃止）したものも除外
        """
        BOUND_TIME = 22  # 境界時間
        all_data = self.find_all_data()
        today = datetime.datetime.now()
        target_date = ""
        if today.hour >= BOUND_TIME:
            #23時を超えている場合
            target_date = today.strftime("%Y%m%d")
        else:
            yesterday = today - timedelta(days=1)
            target_date = yesterday.strftime("%Y%m%d")
        
        contents = []
        for data in all_data:
            if int(data["listingDate"]) <= int(target_date) \
                and data["priceDiary"] is not None:
                contents.append(data)
            continue
        
        response = {
            "contents": contents
        }
        return response