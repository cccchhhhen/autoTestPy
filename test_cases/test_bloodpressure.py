# import pytest
# from utils.http_client import HttpClient
# from utils.db_handler import DBHandler
# @pytest.mark.parametrize("systolic, diastolic, expected_code", [
#     (120, 80, 200),   # 正常值
#     (0, 0, 200),      # 最小值
#     (300, 200, 500),  # 超限值应报错
#     ("abc", 80, 400)  # 类型错误
# ])
# def test_bloodpressure(systolic, diastolic, expected_code):
#     client = HttpClient()
#     data = {"systolic": systolic, "diastolic": diastolic}
#     r = client.post("/api/bloodpressure", data)
    
#     # 断言
#     assert r.status_code == expected_code
#     if expected_code == 200:
#         assert "success" in r.json()["message"]

# def test_db_after_submit():
#     # 先上报数据
#     client = HttpClient()
#     client.post("/api/bloodpressure", {"systolic": 180, "diastolic": 110})
    
#     # 检查数据库
#     db = DBHandler()
#     result = db.query("SELECT * FROM blood_records WHERE systolic > 140")
#     assert len(result) > 0
import pytest
from utils.http_client import HttpClient
from utils.db_handler import DBHandler

def test_db_after_submit():
    """测试数据上报后是否能正确写入数据库"""
    # 1. 上报数据
    client = HttpClient()
    test_data = {"systolic": 190, "diastolic": 100}  # 使用唯一值便于验证
    response = client.post("/api/bloodpressure", test_data)
    assert response.status_code == 200  # 确保接口调用成功

    # 2. 验证数据库
    db = DBHandler()
    # 查询最新插入的记录（按时间倒序）
    result = db.query("""
        SELECT systolic, diastolic 
        FROM blood_records 
        ORDER BY created_at DESC 
        LIMIT 1
    """)
    
    # 3. 断言
    assert len(result) > 0, "数据库未找到新增记录"
    assert result[0][0] == test_data["systolic"], "收缩压数据不匹配"
    assert result[0][1] == test_data["diastolic"], "舒张压数据不匹配"