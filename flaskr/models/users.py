# -*- coding: utf-8 -*-
from sqlalchemy import Column,String, INTEGER
from database import Base,db_session
class Users(Base):
    #查询构造器、、、
    query = db_session.query_property()
    #表名
    __tablename__ ='users'
    #表结构
    id = Column(INTEGER,autoincrement=True,primary_key=True)
    username = Column(String(64),nullable=False)
    passwd = Column(String(64),nullable=False)
    #关联变量名 = relationship('关联表名'，lazy='dynamic'不级联增加，ForeignKey('table.column'))

    def __init__(self,username,passwd):
        self.passwd = passwd
        self.username = username

    def __repr__(self):
        return '<Users %d,%r,%r>' % (self.id, self.username,self.passwd)

