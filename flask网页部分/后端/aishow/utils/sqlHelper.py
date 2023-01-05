import pymysql
from DBUtils.PooledDB import PooledDB

class sqlHelper:
    def __init__(self):
        self.pool = PooledDB(
            pymysql,
            5,
            host='localhost',
            user='root',
            passwd='123',
            db='aitrain',port=3306) #5为连接池里的最少连接数
    def open(self):
        conn = self.pool.connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        return conn,cursor
    def openList(self):
        conn = self.pool.connection()
        cursor = conn.cursor()
        return conn,cursor
    def close(self,conn,cursor):
        cursor.close()
        conn.close()
    def selectTableItems(self,table):
        conn,cursor=self.openList()
        sql=f"select COLUMN_NAME from information_schema.COLUMNS where table_name = '{table}' ORDER BY ordinal_position; ;"
        cursor.execute(sql)
        data=cursor.fetchall()
        self.close(conn,cursor)
        return data
    def selectAll(self,sql,*args):
        conn,cursor=self.open()
        cursor.execute(sql,args)
        data=cursor.fetchall()
        if not data:
            return 'no data'
        self.close(conn,cursor)
        return data
    def excute(self,sql):
        try:
            conn,cursor=self.open()
            cursor.execute(sql)
            conn.commit()
            self.close(conn, cursor)
            return True
        except Exception as e:
            return False

        

        
db=sqlHelper()