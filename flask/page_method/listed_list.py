from dbutils import dbcommon

def get_listed_list():
    """
    /listedList アクセス時のデータを取得して返却する

    return
    ------
    data : dict
        上場データ一覧
    """
    db = dbcommon.DbCommon()
    data = db.find_listed_data()
    return data
