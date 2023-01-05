import json
import warnings

import joblib
import pandas as pd
import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.views import View

from app.models import *

warnings.filterwarnings('ignore')

# 验证登录
def check_login(func):
    def wrapper(request):
        # print("装饰器验证登录")
        cookie = request.COOKIES.get('uid')
        if not cookie:
            return redirect('/login/')
        else:
            return func(request)

    return wrapper

# 数据存放到mysql
def data2sql(request):
    data = pd.read_csv('初始化数据.csv')
    for i in range(len(data)):
        perimeter_worst = data.iloc[i]['perimeter_worst']
        concave_points_worst = data.iloc[i]['concave points_worst']
        area_mean = data.iloc[i]['area_mean']
        radius_worst = data.iloc[i]['radius_worst']
        area_worst = data.iloc[i]['area_worst']
        perimeter_mean = data.iloc[i]['perimeter_mean']
        concave_points_mean = data.iloc[i]['concave points_mean']
        radius_mean = data.iloc[i]['radius_mean']
        concavity_mean = data.iloc[i]['concavity_mean']
        concavity_worst = data.iloc[i]['concavity_worst']
        compactness_worst = data.iloc[i]['compactness_worst']
        area_se = data.iloc[i]['area_se']
        smoothness_worst = data.iloc[i]['smoothness_worst']
        radius_se = data.iloc[i]['radius_se']
        texture_worst = data.iloc[i]['texture_worst']
        diagnosis = data.iloc[i]['diagnosis']
        if not Breast.objects.filter(perimeter_worst=perimeter_worst,concave_points_worst=concave_points_worst,area_mean=area_mean,
                    radius_worst=radius_worst, perimeter_mean=perimeter_mean,concave_points_mean=concave_points_mean,
                                     radius_mean=radius_mean,concavity_mean=concavity_mean,concavity_worst=concavity_worst,
                                     compactness_worst=compactness_worst,area_se=area_se,smoothness_worst=smoothness_worst,
                                     radius_se=radius_se,texture_worst=texture_worst,diagnosis=diagnosis,area_worst=area_worst):
            Breast.objects.create(perimeter_worst=perimeter_worst, concave_points_worst=concave_points_worst,
                                  area_mean=area_mean,
                                  radius_worst=radius_worst, perimeter_mean=perimeter_mean,
                                  concave_points_mean=concave_points_mean,
                                  radius_mean=radius_mean, concavity_mean=concavity_mean,
                                  concavity_worst=concavity_worst,
                                  compactness_worst=compactness_worst, area_se=area_se,
                                  smoothness_worst=smoothness_worst,
                                  radius_se=radius_se, texture_worst=texture_worst, diagnosis=diagnosis,area_worst=area_worst)

    return HttpResponse('操作成功')



# 乳腺癌列表
class daoluList(View):
    def get(self, request):
        uid = int(request.COOKIES.get('uid', -1))
        if uid != -1:
            username = User.objects.filter(id=uid)[0].name


        if 'page' not in request.GET:
            page = 1
        else:
            page = int(request.GET.get('page'))


        data_list = Breast.objects.all()[(page - 1) * 20: page * 20]
        return render(request, 'daoluList.html', locals())

    def post(self, request):

        return JsonResponse({'status': 1, 'msg': '操作成功'})





# @method_decorator(check_login,name='get') #
class predict(View):
    def get(self, request):
        uid = int(request.COOKIES.get('uid', -1))
        if uid != -1:
            username = User.objects.filter(id=uid)[0].name
        # 预测的
        """
        'perimeter_worst',
         'concave points_worst',
         'area_mean',
         'radius_worst',
         'area_worst',
         'perimeter_mean',
         'concave points_mean',
         'radius_mean',
         'concavity_mean',
         'concavity_worst',
         'compactness_worst',
         'area_se',
         'smoothness_worst',
         'radius_se',
         'texture_worst']
        :param request:
        :return:
        """
        info = Breast.objects.all()[0]
        return render(request, 'predict.html', locals())

    def post(self, request):
        data =request.POST.get('data')
        print(data)
        # 'perimeter_worst',
        # 'concave points_worst',
        # 'area_mean',
        # 'radius_worst',
        # 'area_worst',
        # 'perimeter_mean',
        # 'concave points_mean',
        # 'radius_mean',
        # 'concavity_mean',
        # 'concavity_worst',
        # 'compactness_worst',
        # 'area_se',
        # 'smoothness_worst',
        # 'radius_se',
        # 'texture_worst']
        data  = json.loads(data)
        predata = [
            data.get('perimeter_worst'),
            data.get( 'concave_points_worst'),
            data.get( 'area_mean'),
            data.get( 'radius_worst'),
            data.get( 'area_worst'),
            data.get( 'perimeter_mean'),
            data.get( 'concave_points_mean'),
            data.get( 'radius_mean'),
            data.get( 'concavity_mean'),
            data.get( 'concavity_worst'),
            data.get( 'compactness_worst'),
            data.get( 'area_se'),
            data.get( 'smoothness_worst'),
            data.get( 'radius_se'),
            data.get( 'texture_worst'),
        ]
        print(predata)
        predata = [float(item.strip()) for item in predata]
        predata = [predata,]
        # 模型加载
        model = joblib.load('model_5.pkl')
        result = model.predict(predata)[0]
        result = '您预测的结果为：是癌症' if result ==1 else  '您预测的结果为：不是癌症'
        return JsonResponse({'status': 1, 'result': result})



####################################下面可能没用的

@check_login
def my(request):
    uid = int(request.COOKIES.get('uid', -1))
    if uid != -1:
        username = User.objects.filter(id=uid)[0].name
    if request.method == "POST":
        name, tel, password = request.POST.get('name'), request.POST.get('tel'), request.POST.get('password1')
        User.objects.filter(id=uid).update(name=name, tel=tel, password=password)
        return redirect('/')
    else:
        my_info = User.objects.filter(id=uid)[0]
        return render(request, 'my.html', locals())


def test(request):
    return HttpResponse('测试完成')



def login(request):
    if request.method == "POST":
        tel, pwd = request.POST.get('tel'), request.POST.get('pwd')
        if User.objects.filter(tel=tel, password=pwd):

            obj = redirect('/')
            obj.set_cookie('uid', User.objects.filter(tel=tel, password=pwd)[0].id, max_age=60 * 60 * 24)
            return obj
        else:
            msg = "用户信息错误，请重新输入！！"
            return render(request, 'login.html', locals())
    else:
        return render(request, 'login.html', locals())


def register(request):
    if request.method == "POST":
        name, tel, pwd = request.POST.get('name'), request.POST.get('tel'), request.POST.get('pwd')
        # print(name, tel, pwd)
        if User.objects.filter(tel=tel):
            msg = "你已经有账号了，请登录"
        else:
            User.objects.create(name=name, tel=tel, password=pwd)
            msg = "注册成功，请登录！"
        return render(request, 'login.html', locals())
    else:
        msg = ""
        return render(request, 'register.html', locals())


def logout(request):
    obj = redirect('/')
    obj.delete_cookie('uid')
    return obj

################################下面可能没用的




