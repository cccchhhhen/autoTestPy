import pymysql
from config.settings import DB_CONFIG

try:
    conn = pymysql.connect(**DB_CONFIG)
    print("数据库连接成功！")
    conn.close()
except Exception as e:
    print(f"数据库连接失败: {e}")