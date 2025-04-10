import pymysql
from config.settings import DB_CONFIG

class DBHandler:
    def __init__(self):
        self.conn = pymysql.connect(**DB_CONFIG)
        # **DB_CONFIG 将字典解包为关键字参数
        
    def query(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()