# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/28 20:17
@Auth ： rulinma@gmail.com
@File ：run.py
@IDE ：PyCharm
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=5005, debug=True)
    print("run flask app")
