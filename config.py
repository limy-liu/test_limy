"""
配置文件
"""
import logging.handlers
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # 返回当前文件所在文件夹的绝对路径
print(BASE_DIR)

# 能够输出日志信息到控制台和文件; 能够控制日志文件数量及文件大小

# 实例化日志器
logger = logging.getLogger()
# 实例化处理器
sh = logging.StreamHandler()
th = logging.handlers.TimedRotatingFileHandler(filename=BASE_DIR + '/log/info.log',
                                          when='S',
                                          interval=5,
                                          backupCount=4)
# 实例化格式器
fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
formatter = logging.Formatter(fmt)

# 将格式器添加到处理器
sh.setFormatter(formatter)
th.setFormatter(formatter)

# 将处理器提娜佳到日志器
logger.addHandler(sh)
logger.addHandler(th)