from flask import Flask

# 实例化一个Flask
app = Flask(__name__)


# 设置一个网页输出的内容
@app.route('/')
def hello_world():
    return 'Hello,World!'


# 只在测试的时候运行
if __name__ == '__main__':
    # 设置测试使用的端口和ip
    app.run("0.0.0.0", 5000)
