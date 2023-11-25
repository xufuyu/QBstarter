# 从app模块中导入app应用
from app import app
# 获取启动参数
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--host', required=False, default='0.0.0.0', help='Set IP')
parser.add_argument('--port', required=False, default=8000, help='Set Port')
# parser.add_argument('--cuda', action='store_true', help='enables cuda')
opt = parser.parse_args()
host=opt.host
port=opt.port
print("Running at", host, " ", port)
# 启动
if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)



