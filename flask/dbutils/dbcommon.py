from pymongo import MongoClient
from config import config

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
    
    def find_all_data():
        """
        mongoDBに保存されている全データを返す

        return
        ------
        data : dict
            登録済みデータすべてを返す
        """
        data = self.collection.find()
        return data