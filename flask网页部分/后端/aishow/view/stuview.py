import pandas as pd
from flask import Blueprint,request,jsonify
from aishow.utils.sqlHelper import db
from aishow.utils.modelHelper import model

stu=Blueprint('stu',__name__)

@stu.route('/',methods=['GET'])
def selectAll():
    return db.selectAll('select * from stu_score')

@stu.route('/select',methods=['GET'])
def selectClass():
    return db.selectAll('select * from stu_score where class =%s',request.args.get('class'))

@stu.route('/selectSno',methods=['GET'])
def selectSno():
    return db.selectAll('select * from stu_score where sno =%s',request.args.get('sno'))

@stu.route('/delete/<sno>')
def delete(sno):
    res=db.excute(f'delete from stu_score where sno={sno}')
    if  res:
        return '删除成功!'
    return '删除失败!'
    
@stu.route('/update',methods=["GET","POST"])
def update():
    try :
        row = request.get_json(silent=True)['data']
        chinese = row.get('chinese')
        math = row['math']
        sno = row.get('sno')
        pre = model.predictStu(chinese, math)
        db.excute(f'update stu_score set math={math},chinese={chinese},class="{pre}" where sno={sno}')
        return '修改数据成功!'
    except Exception as e :
        return '修改数据失败!'
    

@stu.route('/upload',methods=["GET","POST"])
def upload():
    try:
        file = request.files.getlist('file')[0]
        upload_dataset = pd.read_csv(file)
        lis=['Chinese','Math']
        for i in lis:
            if i not in upload_dataset.columns:
                return '请保持导入数据的字段中含有Chinese和Math字段'
        for i in range(upload_dataset.shape[0]):
            row=upload_dataset.iloc[i]
            chinese=row['Chinese']
            math=row['Math']
            pre=model.predictStu(chinese,math)
            db.excute(f'insert into stu_score(chinese,math,class) values({chinese},{math},"{pre}")')
            
        return 'import success!'
    except Exception as e:
        return '请导入正确格式'
    
    
@stu.route('/delete')
def deleteAll():
    res=db.excute('TRUNCATE TABLE stu_score ')
    if  res:
        return '删除成功!'
    return '删除失败!'
@stu.route('/add',methods=['POST','GET'])
def addData():
    try:
        row=request.get_json(silent=True)['data']
        chinese = row.get('chinese')
        math = row['math']
        sno=row.get('sno')
        pre = model.predictStu(chinese, math)
        if sno:
            db.excute(f'insert into stu_score(sno,chinese,math,class) values({sno},{chinese},{math},"{pre}")')
        else:
            db.excute(f'insert into stu_score(chinese,math,class) values({chinese},{math},"{pre}")')
        return '插入数据成功!'
    except Exception as e:
        return '插入数据失败!'