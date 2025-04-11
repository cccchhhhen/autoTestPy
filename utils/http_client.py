import requests
import logging
from config.settings import BASE_URL
from config.logging import setup_logging
# 初始化日志配置
setup_logging() # 强制覆盖 pytest 的默认配置
logger = logging.getLogger(__name__)
class HttpClient:
    def post(self, endpoint, data):
        url = f"{BASE_URL}{endpoint}"
        try:
            return requests.post(url, json=data, timeout=5)
        except requests.exceptions.Timeout as e:
            logger.error(f"登录请求超时: {e}")
            return None
        except requests.exceptions.RequestException as e:
            logger.error(f"登录请求失败: {e}")
            return None