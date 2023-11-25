from app import app
import logging
import requests
"""from flask import request
import threading
thread = threading.Thread(target=def, args=())
thread.start()
"""
"""
alpha：内部版本
beta：测试版
lts：长期维护版本
release：发行版
dev：开发版本号
"""
__X__=str(0)
__Y__=str(0)
__Z__=str(0)
__N__=str(1)
__V__="dev"
__VERSION__=".".join([__X__,__Y__,__Z__,__V__,__N__])

def get_version_number():
    return __VERSION__


# 设置flask日志（关闭FLASK的日志）
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
def detect_updates():
    version_request = requests.request("GET", "http://guppy.ltd:8005")
    version_number = version_request.text
    return {"version_updates":version_number,"version_current":get_version_number()}
print(detect_updates())
@app.route("/", methods=("GET", "POST"))
def get_index():
    return 'Hello QB-starter!'

@app.route("/version", methods=("GET", "POST"))
def get_version():
    return detect_updates()
