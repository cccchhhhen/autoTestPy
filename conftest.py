# E:\medical_api_test\conftest.py
import pytest
from utils.db_mysql import MySQLHandler
from config.settings import DB_CONFIG

@pytest.fixture
def db():
    """提供数据库连接的fixture"""
    handler = MySQLHandler(**DB_CONFIG)
    
    # 初始化测试表
    handler.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE,
            password VARCHAR(50),
            last_login DATETIME
        )
    """)
    yield handler
    
    # 测试后清理
    # handler.execute("TRUNCATE TABLE users")
    handler.close()