from dbutils import dbcommon

def get_listed_companies(securities_no):
    """
    /getDetail/<securities_no> アクセス時のデータを取得して返却する

    return
    ------
    data : dict
        証券コードに該当するデータ
    """
    db = dbcommon.DbCommon()

    # 対象データの全取得
    return db.find_one_from_securities_no(securities_no)
