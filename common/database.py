import pymongo


class Database(object):
    # 建立與localhost port 27017連線
    URI = ['localhost:27017']
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        # 設定使用的資料庫
        Database.DATABASE = client['project']

    @staticmethod
    # 新增
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    # 查詢
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)