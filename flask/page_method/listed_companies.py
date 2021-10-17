from dbutils import dbcommon

def get_listed_companies(day_count):
    """
    /listedCompanys/<day_count> アクセス時のデータを取得して返却する

    return
    ------
    data : dict
        上場データ一覧
    """
    day_cnt = int(day_count)
    db = dbcommon.DbCommon()

    # 対象データの全取得
    data = db.find_listed_data()

    # 指定日数分にデータを整形
    for one_data in data:
        price_diary = list(one_data["priceDiary"])
        while len(price_diary) < day_cnt:
            price_diary.append(["-","-","-","-","-","-","-","-"])
        
        one_data["priceDiary"] = price_diary[0:day_cnt]
        
    return data