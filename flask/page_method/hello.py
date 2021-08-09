from dbutils import dbcommon

def getHello():
    """
    /hello アクセス時のデータを取得して返却する

    return
    ------
    data : dict
        サンプル用データ
    """
    db = dbcommon.DbCommon()
    data = db.find_one_from_securities_no("6227")
    return data