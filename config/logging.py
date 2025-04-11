import logging
import os
def setup_logging():
    # # 获取根记录器
    # root_logger = logging.getLogger()
    
    # # 移除所有现有处理器
    # for handler in root_logger.handlers[:]:
    #     root_logger.removeHandler(handler)

    # 原始拼接路径
    raw_path = os.path.join(os.path.dirname(__file__), "..", "app.log")
    # 规范化处理
    normalized_path = os.path.normpath(raw_path)
    # print(f"日志文件路径: {normalized_path}")
    logging.basicConfig(
        filename=normalized_path,
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True
    )
# # 可选：添加控制台输出
#     console_handler = logging.StreamHandler()
#     console_handler.setLevel(logging.WARNING)
#     logging.getLogger().addHandler(console_handler)