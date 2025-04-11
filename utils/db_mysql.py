import pymysql
from pymysql.cursors import DictCursor
import pytest

class MySQLHandler:
    def __init__(self, host, user, password, database):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            cursorclass=DictCursor,
            autocommit=False
        )
    
    def execute(self, sql, params=None):
        """执行写操作(INSERT/UPDATE/DELETE)"""
        with self.conn.cursor() as cursor:
            cursor.execute(sql, params or ())
            self.conn.commit()
            return cursor.rowcount
    
    def query(self, sql, params=None):
        """执行查询操作"""
        with self.conn.cursor() as cursor:
            cursor.execute(sql, params or ())
            return cursor.fetchall()
    
    def close(self):
        self.conn.close()
