import mysql.connector

def create_database():
    conn = mysql.connector.connect(user='root',password='123',database='test')
    cursor = conn.cursor()

    sql = '''create table USER
             (id VARCHAR(10) PRIMARY KEY ,
             stuname VARCHAR(20))'''

    cursor.execute(sql)
    conn.commit()
    cursor.close()

def drop_database():
    conn = mysql.connector.connect(user='root', password='123', database='test')
    cursor = conn.cursor()

    sql = '''drop table USER'''
    cursor.execute(sql)
    conn.commit()
    cursor.close()

if __name__ == '__main__':
    create_database()
    #drop_database()
