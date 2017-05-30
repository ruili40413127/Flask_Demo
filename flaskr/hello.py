# -*- coding: utf-8 -*-
from flask import Flask, request
app = Flask(__name__)


#route() 装饰器告诉 Flask 什么样的URL 能触发我们的函数。
#一个函数绑定一个url
'''
url中的变量部分用<variable_name>标记，且name前面可用coverter:进行类型转换；
可以转换的类型有 int float path（与默认str类似，但是接受斜线）
'''
@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method =='GET':
        return 'Hello World!'
    else:
        return 'What?'
'''
重定向行为：
/url1/ 相比/url2 ，若不带斜线访问url1，会被重定向到带斜线的规范url去，
但是对url2,访问带斜线的url则会404错误
'''


if __name__ == '__main__':
    app.run(debug=True)

#生成url：
with app.test_request_context():
    print url_for('hello_world', next='/')#第一个参数是构建的url对应的函数名，
    #之后的参数为url参数，这样生成的好处不仅描述性好，而且会转义特殊字符和unicode
    #还会自动匹配对应的根路径
                  
