import time
import os
import logging

cur_read_count = 0
log_file_path = "/tmp/log/app.log"


# 模拟将日志数据上报到数据中心
def report_to_center(logs):
    if len(logs) != 0:
        logging.info("上报 " + str(len(logs)) + " 条日志到数据中心")
    else:
        logging.info("没有新增日志，无需上报")


# 从文件读取日志并上报到数据中心
def collect_log():
    global cur_read_count

    if os.path.exists(log_file_path) == False:
        logging.info("log file %s not exists!" % (log_file_path))
        return

    f = open(log_file_path, "r")
    f.seek(cur_read_count)

    logs = []
    line = f.readline()
    while line:
        logs.append(line)
        cur_read_count += len(line)
        line = f.readline()

    f.close()
    report_to_center(logs)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.INFO)
    logging.info("start collect logs")

    while True:
        collect_log()
        time.sleep(10)
