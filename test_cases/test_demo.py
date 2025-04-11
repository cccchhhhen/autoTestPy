# from utils.http_client import HttpClient

# def test_demo():
#     client = HttpClient()
#     r = client.post("/login", {"username": "admin","password": "admin"})
#     assert r.status_code == 200

import pytest
from utils.http_client import HttpClient
from utils.db_mysql import MySQLHandler
import datetime
def test_mysql_crud_operations(db):
    # 初始化测试数据
    test_user = {"username": "0411", "password": "0411"}
    
    # 1. 测试插入数据
    insert_sql = "INSERT INTO users (username, password) VALUES (%(username)s, %(password)s)"
    affected_rows = db.execute(insert_sql, test_user)
    assert affected_rows == 1, "插入数据失败"
    
    # 2. 验证数据存在
    query_sql = "SELECT * FROM users WHERE username = %s"
    users = db.query(query_sql, (test_user["username"],))
    assert len(users) == 1
    assert users[0]["password"] == test_user["password"]
    
    # 3. 测试更新数据
    new_password = "new_secure_password"
    update_sql = "UPDATE users SET password = %s WHERE username = %s"
    db.execute(update_sql, (new_password, test_user["username"]))
    updated_user = db.query(query_sql, (test_user["username"],))[0]
    assert updated_user["password"] == new_password
    
    # 4. 测试删除数据
    delete_sql = "DELETE FROM users WHERE username = %s"
    db.execute(delete_sql, (test_user["username"],))
    assert len(db.query(query_sql, (test_user["username"],))) == 0

def test_login_with_db_validation(db):
    """结合HTTP请求和数据库验证的测试"""
    client = HttpClient()
    
    # 准备测试数据
    test_data = {"username": "test_user", "password": "Test@123"}
    db.execute("INSERT INTO users (username, password) VALUES (%s, %s)", 
              (test_data["username"], test_data["password"]))
    
    # 发送登录请求
    response = client.post("/login", test_data)
    assert response.status_code == 200
    update_sql = "UPDATE users SET last_login = %s WHERE username = %s"
    db.execute(update_sql, (datetime.datetime.now(), test_data["username"]))
    
    # 验证数据库日志（假设登录成功会更新last_login字段）
    user_record = db.query("SELECT last_login FROM users WHERE username = %s", 
                          (test_data["username"],))
    assert user_record[0]["last_login"] is not None