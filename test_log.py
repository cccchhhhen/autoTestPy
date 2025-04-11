from config.logging import setup_logging
# 初始化日志配置
setup_logging()
import logging
logger = logging.getLogger(__name__)
def test_log():
    logger.error("今天是阴天！")
test_log()