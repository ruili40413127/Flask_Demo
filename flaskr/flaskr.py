# -*- coding: utf-8 -*-
from flask import Flask,request,render_template,url_for,session,escape,redirect,make_response
from database import db_session,db_engine,db_metadata
from models import entries,users
from sqlalchemy import Table
from middleware import LoinRequired,hasLogged
from controller.loginController import loginController
import json

app=Flask(__name__)
app.config.from_object('config')


@app.route('/',methods=['GET'])
@LoinRequired #使用中间件保证必须登录
def welcome():
    print 'in welcome'
    return render_template('index.html')

#登出，修改session并返回响应到前端
@app.route('/logout/',methods=['POST'])
@LoinRequired #使用中间件
def logout():
    print 'logout'
    session.pop('username',None)
    resp = {"successed": True}
    resp = json.dumps(resp)
    return resp

@app.route('/login/',methods=['GET','POST'])
@hasLogged
def login():
    print 'in request'
    print request.method
    print request.headers
    if request.method=='GET': #GET方法访问时，直接返回登录页
        return render_template('login.html')
    if request.method=='POST':#POST方法时，做登陆验证
        print 'forms=',request.form['username'],request.form['passwd']
        res = False
        controller =  loginController()
        res = controller.check_login(request.form['username'],request.form['passwd'])
        #根据检查数据库的结果返回登录请求的结果
        #下面这一段可以都写到控制器里面
        if(res == False):
            resp = {"message":"登录失败，请重试", "successed":False}
            resp = json.dumps(resp)
            #print resp
            return resp
        else:#登录验证成功
            session['username'] = request.form['username']#记下已经登陆的用户
            resp = {"successed":True}
            resp = json.dumps(resp)
            return resp

#注册，将请求内容查数据库，返回回应的json
@app.route('/register/',methods=['POST'])
def register():
    print 'forms=', request.form['username'], request.form['passwd']
    controller = loginController()
    resp = controller.register(request.form['username'], request.form['passwd'])
    resp = json.dumps(resp)
    return resp



if __name__ == '__main__':
    app.run(debug=True)
    '''new = Entries(title='in?', text="test in")
    
    #插入
    db_session.add(new)
    db_session.flush()
    
    #查找
    entries = Entries.query.filter(Entries.id==3).all()
    print entries
    #删除，一次只对一个确定的实例
    db_session.delete(entries[0])
    db_session.flush()
    '''
    '''''
    table = Table('entries',metadata,autoload=True)
    #可以通过创建连接
    conn = db_engine.connect()
    #之后
    conn.execute(table.update(),)
    '''