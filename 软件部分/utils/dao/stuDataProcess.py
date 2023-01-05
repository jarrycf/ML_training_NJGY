import pandas as pd
import pymysql
from config.config import *
import csv



class StuDataProcess:
    def __init__(self):
        # 连接数据库
        self.conn = pymysql.connect(
            host=IPADDRESS,
            user=USERNAME,
            password=PASSWORD,
            db=DB
        )
        # 获得游标
        self.cursor = self.conn.cursor()
    def insertData(self,filename):
        try:
            data=pd.read_csv(filename)
            shape=data.shape
            if shape[1]==3:
                for i in range(shape[0]):
                    # 插入数据
                    sql = "insert into stu_score(sno,chinese,math) values( % d, % d, % d)"
                    indata = (data.iloc[:,0][i], data.iloc[:,1][i], data.iloc[:,2][i])
                    self.cursor.execute(sql % indata)
                    self.conn.commit()
                return 'import success!'
            elif shape[1]==2:
                for i in range(shape[0]):
                    # 插入数据
                    sql = "insert into stu_score(chinese,math) values( % d, % d)"
                    indata = (data.iloc[:,0][i], data.iloc[:,1][i])
                    self.cursor.execute(sql % indata)
                    self.conn.commit()
                return 'import success!'
            elif shape[1]==4:
                for i in range(shape[0]) :
                    # 插入数据
                    sql = "insert into stu_score values( % d, % d, % d,'%s')"
                    indata = (data.iloc[:, 0][i], data.iloc[:, 1][i], data.iloc[:, 2][i],data.iloc[:, 3][i])
                    self.cursor.execute(sql % indata)
                    self.conn.commit()
                return 'import success!'
        except Exception as e:
            return e
    
    def insertRow(self,sno,math,chinese):
        try:
            # 插入
            sql = "insert into stu_score(sno,chinese,math) values( % d, % d, % d)"
            self.cursor.execute(sql % (sno,math,chinese))
            self.conn.commit()
            return 'insert success!'
        except Exception as e:
            return str(e)
    def selectSno(self,sno):
        sql = "select * from stu_score  where sno=%d"
        self.cursor.execute(sql % sno)
        res=self.cursor.fetchone()
        self.conn.commit()
        if res:
            return f"""
    学号:{res[0]}
    Chinese:{res[1]},
    Math:{res[2]},
    Class:{res[3]}
            """

    def removeRow(self,sno):
        # 删除数据
        sql = "delete from stu_score  where sno=%d"
        self.cursor.execute(sql % sno)
        self.conn.commit()
    def updateSingleData(self,data):
            # 插入数据
            sql = "update  stu_score  set class='%s' where sno=%d"
            indata = (data[3],data[0])
            self.cursor.execute(sql % indata)
            self.conn.commit()
    def deleteData(self):
        try:
            sql = " TRUNCATE table stu_score "
            self.cursor.execute(sql)
            self.conn.commit()
            return 'delete success!'
        except Exception as e:
            return e
    def outputData(self):
        f = open('data/output.csv', 'w', encoding='utf-8')
        csv_writer = csv.writer(f)
        csv_writer.writerow(["学号", "语文成绩", "数学成绩",'类别'])
        try:
            sql="select * from stu_score"
            self.cursor.execute(sql)
            for row in self.cursor.fetchall() :
                csv_writer.writerow(row)
            self.conn.commit()
            return 'output success!'
        except Exception as e:
            return e


        