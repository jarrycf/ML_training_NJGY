import datetime
import random

import pandas as pd
from flask import Blueprint, request, jsonify

from aishow.utils.sqlHelper import db
from aishow.utils.strFormatHelper import isNone
from aishow.utils.modelHelper import model

home = Blueprint('home', __name__)


@home.route('/', methods=['GET'])
def selectAll() :
    return db.selectAll('select * from home_score')


@home.route('/select', methods=['GET'])
def selectClass() :
    return db.selectAll('select * from home_score where class =%s', request.args.get('class'))


@home.route('/selectSno', methods=['GET'])
def selectSno() :
    return db.selectAll('select * from home_score where id =%s', request.args.get('sno'))


@home.route('/delete/<sno>')
def delete(sno) :
    print(f'delete from home_score where id={sno}')
    res = db.excute(f'delete from home_score where id={sno}')
    if res :
        return '删除成功!'
    return '删除失败!'


@home.route('/update', methods=["GET", "POST"])
def update() :
    try :
        row = request.get_json(silent=True)['data']
        house_age = float(row.get('house_age'))
        nearest_mrt = float(row.get('nearest_mrt'))
        stores = float(row.get('stores'))
        pre = model.predictHome(house_age,nearest_mrt,stores)
        id=int(row.get('id'))
        db.excute(f'update home_score set nearest_mrt={nearest_mrt},stores={stores},house_age={house_age},price_area={pre} where id={id}')
        return '修改数据成功!'
    except Exception as e :
        return '修改数据失败!'


@home.route('/upload', methods=["GET", "POST"])
def upload() :
    try :
        file = request.files.getlist('file')[0]
        upload_dataset = pd.read_csv(file)
        lis = ['house_age','nearest_mrt','stores']
        for i in lis :
            if i not in upload_dataset.columns :
                return f'请保持导入数据的字段中含有{",".join(lis)}字段'
        for i in range(upload_dataset.shape[0]) :
            row = upload_dataset.iloc[i]
            house_age = row['house_age']
            nearest_mrt = row['nearest_mrt']
            stores = row['stores']
            pre = model.predictHome(house_age,nearest_mrt,stores)
            db.excute(f'insert into home_score(nearest_mrt,house_age,stores,price_area) values({nearest_mrt},{house_age},{stores},{pre})')
        
        return 'import success!'
    except Exception as e :
        return '请导入正确格式'


@home.route('/delete')
def deleteAll() :
    res = db.excute('TRUNCATE TABLE home_score ')
    if res :
        return '删除成功!'
    return '删除失败!'


@home.route('/add', methods=['POST', 'GET'])
def addData() :
    # try :
        row = request.get_json(silent=True)['data']
        id=int(row.get('id'))
        house_age=float(row.get('house_age'))
        nearest_mrt=float(row.get('nearest_mrt'))
        stores=float(row.get('stores'))
        if isNone(house_age,nearest_mrt,stores):
            return "数据不能为空!"
        if not id:
            id=random.randint(1,1000)
        pre = model.predictHome(house_age,nearest_mrt,stores)

        db.excute(
            f"insert into home_score VALUES ({id},{house_age},{nearest_mrt},{stores},{pre})"
        )
        return '插入数据成功!'
    # except Exception as e :
    #     return '插入数据失败!'