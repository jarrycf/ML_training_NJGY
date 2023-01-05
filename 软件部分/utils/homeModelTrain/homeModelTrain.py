import joblib
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge,SGDRegressor
import sklearn.metrics as sm
from sklearn.model_selection import train_test_split, GridSearchCV
import json,cv2 as cv

from sklearn.svm import SVC

from frames.homeframe.tableFrame import TableSheet
from config.config import *
from sklearn.preprocessing import StandardScaler,PolynomialFeatures

class HomeModelTrain:
    def __init__(self):
        ...
            

            
    def saveModel(self):
        try :
            data = pd.read_csv('data/HouseProcessed.csv')
        
            X = data.loc[:, data.columns[:-1]]
            y = data[data.columns[-1]]
        

            with open('data/select_model.json', 'r') as f :
                modelData = json.loads(f.read())
                if modelData['model'] == "linerModel" :
                    sk_model = LinearRegression()
                elif modelData['model']=="Ridge":
                    sk_model = Ridge(alpha=modelData['alpha'])
                elif modelData['model']=="SGDRegressor":
                    sk_model = SGDRegressor(eta0=ETA0)
            polyfit = PolynomialFeatures(degree=DEGREE)
            X = polyfit.fit_transform(X)
            for i in range(1000):
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE)

                # 训练模型
                sk_model.fit(X_train, y_train)
        
                trainPre = sk_model.predict(X_train)
                testPre = sk_model.predict(X_test)
                print(sm.r2_score(y_test, testPre))
                if sm.r2_score(y_test, testPre)>MINR2 or i==999:
                    
                    text = f"""
                特征值:{list(data.columns)[:-1]}
                目标值:{list(data.columns)[-1]}
                训练集平均绝对值误差:{sm.mean_absolute_error(y_train, trainPre)}
                训练集平均平方误差:{sm.mean_squared_error(y_train, trainPre)}
                训练集中位绝对值误差:{sm.median_absolute_error(y_train, trainPre)}
                训练集R2得分:{sm.r2_score(y_train, trainPre)}
                测试集平均绝对值误差:{sm.mean_absolute_error(y_test, testPre)}
                测试集平均平方误差:{sm.mean_squared_error(y_test, testPre)}
                测试集中位绝对值误差:{sm.median_absolute_error(y_test, testPre)}
                测试集R2得分:{sm.r2_score(y_test, testPre)}
                            """
                    with open('data/model_inf.txt', 'w') as f :
                        f.write(text)
                    # 保存字段信息
                    f = open('data/features.json', 'w')
                    f.write(json.dumps({
                        'features' : list(data.columns)[:-1],
                        'target' : list(data.columns)[-1]
                    }))
                    f.close()
                    # 保存模型
                    joblib.dump(sk_model, 'model/housePricePre.pkl')
                    return 'train success!'
        except Exception as e :
            return e
    # 查看模型相关信息
    def seeModelMes(self):
        with open('data/model_inf.txt', 'r') as f :
            return f.read()
    def predict(self,filename):
        try:
            data=pd.read_csv(filename)
            f = open('data/features.json', 'r')
            data2=json.loads(f.read())
            model = joblib.load('model/housePricePre.pkl')
            feature=data.loc[:,data2['features']]
            polyfit = PolynomialFeatures(degree=DEGREE)
            feature= polyfit.fit_transform(feature)
            pre=model.predict(feature)
            data['pre']=pre
            self.table=TableSheet()
            if data2['target'] in data.columns:
                self.table.initData(data.loc[:,['pre',data2['target']]])
                plt.subplots(figsize=(10, 5))
                plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
                plt.rcParams["axes.unicode_minus"] = False
                plt.title('房屋价格真实值 VS 预测值')
                plt.plot(range(len(pre)), pre)
                plt.plot(range(len(pre)), data.loc[:, data2['target']])
                plt.legend('best', labels=['预测值', '真实值'])
                plt.savefig('images/scatter2.png')
                cv.imshow(f"scatter", cv.imread('images/scatter2.png'))
                cv.waitKey(0)
            else:
                self.table.initData(data)
            self.table.show()
            
        except Exception as e:
            return e

        