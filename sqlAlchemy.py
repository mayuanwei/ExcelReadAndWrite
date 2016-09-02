from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class User(base):
    __tablename__ = 'user'

    id = Column(String(10),primary_key=True)
    stuname = Column(String(20))

def add_data(session):
    new_user = User(id='3',stuname='adm')
    session.add(new_user)
    session.commit()
    session.close()

def query_data(session):
    #创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行
    user = session.query(User).filter(User.id=='2').one()
    print(type(user))
    print(user.stuname)
    session.close()

if __name__ == '__main__':
    #'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
    engine = create_engine("mysql+mysqlconnector://root:123@localhost:3306/test")
    #DBsession = sessionmaker(bind=engine)
    #session = DBsession()
    session = Session(bind=engine)
    add_data(session)
    query_data(session)
    #print(type(session))
    #print(type(DBsession))
