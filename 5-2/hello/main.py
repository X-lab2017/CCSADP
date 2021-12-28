from flask import Flask
import logging
import os


# 日志文件
log_file_path = '/tmp/log/app.log'

# 初始化环境变量
pod_name = os.environ.get("POD_NAME")
pod_ip = os.environ.get("POD_IP")

# 实例化一个Flask
app = Flask(__name__)


# 设置一个网页输出的内容
@app.route('/')
def hello_world():
    app.logger.info('call hello')
    return 'Hello World! [ServerInfo: PodName=%s, PodIP=%s]' % (pod_name, pod_ip)


# 设置输出日志到指定的文件和控制台
def init_log():
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')

    file_handler = logging.FileHandler(log_file_path, encoding='UTF-8')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging_format)

    app.logger.setLevel('INFO')
    app.logger.addHandler(file_handler)


# 只在测试的时候运行
if __name__ == '__main__':
    # 初始化日志
    init_log()

    # 设置测试使用的端口和ip
    app.run("0.0.0.0", 5000)
