import datetime
import random

import pandas as pd
from flask import Blueprint, request, jsonify

from aishow.utils.sqlHelper import db
from aishow.utils.strFormatHelper import isNone
from aishow.utils.modelHelper import model

medical = Blueprint('medical', __name__)


@medical.route('/', methods=['GET'])
def selectAll() :
    return db.selectAll('select * from medical_score')


@medical.route('/select', methods=['GET'])
def selectClass() :
    return db.selectAll('select * from medical_score where class =%s', request.args.get('class'))


@medical.route('/selectSno', methods=['GET'])
def selectSno() :
    return db.selectAll('select * from medical_score where id =%s', request.args.get('sno'))


@medical.route('/delete/<sno>')
def delete(sno) :
    print(f'delete from medical_score where id={sno}')
    res = db.excute(f'delete from medical_score where id={sno}')
    if res :
        return '删除成功!'
    return '删除失败!'


@medical.route('/update', methods=["GET", "POST"])
def update() :
    try :
        row = request.get_json(silent=True)['data']
        id = int(row.get('id'))
        menopause = row.get('menopause')
        age = row.get('age')
        tumor_size = row.get('tumor_size')
        inv_nodes = row.get('inv_nodes')
        node_caps = row.get('node_caps')
        deg_malig = row.get('deg_malig')
        breast_quad = row.get('breast_quad')
        irradiat = row.get('irradiat')
        pre = model.predictMedical(age, menopause, tumor_size, inv_nodes, node_caps, deg_malig, breast_quad, irradiat)
        if pre :
            pre = 'recurrence-events'
        else :
            pre = 'no-recurrence-events'
        db.excute(
            f'update medical_score set \
            age="{age}",menopause="{menopause}",tumor_size="{tumor_size}",inv_nodes="{inv_nodes}",\
            node_caps="{node_caps}",deg_malig="{deg_malig}",breast_quad="{breast_quad}",irradiat="{irradiat}",class="{pre}" where id={id}')
        return '修改数据成功!'
    except Exception as e :
        return '修改数据失败!'


@medical.route('/upload', methods=["GET", "POST"])
def upload() :
    # try :
        file = request.files.getlist('file')[0]
        upload_dataset = pd.read_csv(file)
        lis = ['age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'deg-malig', 'breast-quad','irradiat']
        for i in lis :
            if i not in upload_dataset.columns :
                return f'请保持导入数据的字段中含有{",".join(lis)}字段'
        for i in range(upload_dataset.shape[0]) :
            row = upload_dataset.iloc[i]
            menopause = row['menopause']
            age = row['age']
            tumor_size = row['tumor-size']
            inv_nodes = row['inv-nodes']
            node_caps = row['node-caps']
            deg_malig = row['deg-malig']
            breast_quad = row['breast-quad']
            irradiat = row['irradiat']
            pre = model.predictMedical(age, menopause, tumor_size, inv_nodes, node_caps, deg_malig, breast_quad,irradiat)
            if pre :
                pre = 'recurrence-events'
            else :
                pre = 'no-recurrence-events'
            db.excute(f"insert into medical_score(age, menopause, tumor_size, inv_nodes, node_caps, deg_malig, breast_quad,irradiat,class) values('{age}','{menopause}','{tumor_size}','{inv_nodes}','{node_caps}','{deg_malig}','{breast_quad}','{irradiat}','{pre}')")
            print(f"insert into medical_score(age, menopause, tumor_size, inv_nodes, node_caps, deg_malig, breast_quad,irradiat,class) values('{age}','{menopause}','{tumor_size}','{inv_nodes}','{node_caps}','{deg_malig}','{breast_quad}','{irradiat}','{pre}')")
        return 'import success!'
    # except Exception as e :
    #     return '请导入正确格式'
@medical.route('/delete')
def deleteAll() :
    res = db.excute('TRUNCATE TABLE medical_score ')
    if res :
        return '删除成功!'
    return '删除失败!'
@medical.route('/add', methods=['POST', 'GET'])
def addData() :
    # try :
    row = request.get_json(silent=True)['data']
    id = int(row.get('id'))
    menopause =row.get('menopause')
    age =row.get('age')
    tumor_size =row.get('tumor_size')
    inv_nodes =row.get('inv_nodes')
    node_caps =row.get('node_caps')
    deg_malig =row.get('deg_malig')
    breast_quad =row.get('breast_quad')
    irradiat =row.get('irradiat')
    if isNone(menopause, age, tumor_size, node_caps, inv_nodes, irradiat, deg_malig, breast_quad) :
        return "数据不能为空!"
    if not id :
        id = random.randint(1, 1000)
    pre = model.predictMedical(age, menopause, tumor_size, inv_nodes,node_caps, deg_malig, breast_quad,irradiat)
    if pre:
        pre='recurrence-events'
    else:
        pre = 'no-recurrence-events'
    res=db.excute(
        f"insert into medical_score VALUES ({id},'{age}','{menopause}','{tumor_size}','{inv_nodes}','{node_caps}','{deg_malig}','{breast_quad}','{irradiat}','{pre}')"
        )
    print(        f"insert into medical_score VALUES ({id},'{age}','{menopause}','{tumor_size}','{inv_nodes}','{node_caps}','{deg_malig}','{breast_quad}','{irradiat}','{pre}')")
    if res:
        return '插入数据成功!'
    else:
        return '插入数据失败!'
# except Exception as e :
#     return '插入数据失败!'

