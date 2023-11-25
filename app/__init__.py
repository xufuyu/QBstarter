from flask import Flask
# 创建app应用,__name__是python预定义变量，被设置为使用本模块.
app = Flask(__name__)
from app import routes
