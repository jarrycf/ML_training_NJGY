import json
import os
import cv2 as cv
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
# 支持向量机
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from config.config import *
from frames.medicalframe.tableFrame import TableSheet
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

class MedicalModelTrain:
    def __init__(self):
        self.predictDict={
            'age':['10-19', '20-29', '30-39','40-49','50-59','60-69','70-79', '80-89','90-99'],
            'menopause':['lt40', 'ge40', 'premeno'],
            'tumor-size':['0-4', '5-9', '10-14', '15-19', '20-24', '25-29','30-34','35-39', '40-44','45-49', '50-54', '55-59'],
            'inv-nodes':['0-2', '3-5', '6-8','9-11', '12-14', '15-17', '18-20', '21-23','24-26', '27-29', '30-32', '33-35','36-39'],
            'node-caps':['yes', 'no'],
            'deg-malig':['1', '2','3'],
            'breast-quad':['left-up', 'left-low', 'right-up', 'right-low', "central"],
            'irradiat':['yes','no'],
            
        }
    def predict(self,filename):
        try:

            data=pd.read_csv(filename)
            with open(MEDICALFEATURESANDTARGET,'r') as f:
                    data2=json.loads(f.read())
            print(data2)
            model = joblib.load(MEDICALMODELPATH)
            with open('data/trainData.txt','r') as f:
                trainData=json.loads(f.read())
            print(trainData)
            le = preprocessing.LabelEncoder()
            
            for feature in trainData['labelEncoder'] :
                # 非数字型和数字型标签值标准化
                print(le.fit_transform(self.predictDict[feature]))
                data[feature] = le.transform(data[feature])
            feature=data.loc[:,data2['features']]
            pre=model.predict(feature)
            data['pre']=pre
            self.table=TableSheet()
            if trainData['target'] in data.columns:
                self.table.initData(data.loc[:,['pre',trainData['target']]])
                plt.subplots(figsize=(10, 5))
                plt.scatter(range(len(pre)), pre, c='green')
                plt.scatter(range(len(pre)), data.loc[:, data2['target']])
                plt.legend('best', labels=['preValue', 'tarValue'])
                plt.savefig('images/scatter2.png')
                cv.imshow(f"scatter", cv.imread('images/scatter2.png'))
                cv.waitKey(0)
            else:
                self.table.initData(data)
            self.table.show()
           
        except Exception as e:
            return e
    def saveModel(self):
        try:
            if not os.path.exists('data/trainData.txt'):
                return 'no'
            with open('data/trainData.txt','r') as f:
                trainData=json.loads(f.read())
            data=pd.read_csv(MEDICALDATAPATH)
            with open('data/select_model2.json', 'r') as f :
                modeldata = json.loads(f.read())
            target=''
            feature=''
            if trainData['target'] and trainData['target'] in data.columns:
                pre=data.drop([trainData['target']],axis=1)
                
                X_train, X_test, y_train, y_test = train_test_split(pre, data[trainData['target']], test_size=modeldata['testSize'],
                                                                random_state=1)
                with open(MEDICALFEATURESANDTARGET, 'w') as f :
                    target=f"target : {trainData['target']}"
                    feature=f"features : {list(pre.columns)}"
                    f.write(json.dumps(
                        {
                            'features' : list(pre.columns),
                            'target' : trainData['target']
                        }
                    ))
            else:
                X_train, X_test, y_train, y_test = train_test_split(data[data.columns[:-1]], data[data.columns[-1]], test_size=TEST_SIZE,
                                                                random_state=1)
                with open(MEDICALFEATURESANDTARGET, 'w') as f :
                    f.write(json.dumps(
                        {
                            'features' : list(data.columns[:-1]),
                            'target' : data.columns[-1]
                        }
                    ))

            if modeldata['model']=='DecisionTreeClassifier':
                max_depth = range(4, 10, 1)
                min_samples_split = range(2, 12, 1)
                min_samples_leaf = range(2, 12, 1)
                parameters_dtc = {'max_depth' : max_depth, 'min_samples_split' : min_samples_split,
                                  'min_samples_leaf' : min_samples_leaf}
    
                grid_search = GridSearchCV(estimator=DecisionTreeClassifier(), param_grid=parameters_dtc, cv=10,
                                           n_jobs=-1)
                grid_search.fit(X_train, y_train)
                # print(grid_search.best_estimator_)
                # 根据调参结果构建决策树
                dtc = grid_search.best_estimator_
                dtc.fit(X_train, y_train)
                y_predict = dtc.predict(X_test)
                
                text=f"""
        决策树模型在测试集上的准确率为：", {metrics.accuracy_score(y_test, y_predict)}
        决策树模型在训练集上的准确率为：", {metrics.accuracy_score(y_train, dtc.predict(X_train))}
        features : {list(data.columns[:-1])},
        target : {data.columns[-1]}
                """
                if target and feature:
                    text = f"""
                    决策树模型在测试集上的准确率为：", {metrics.accuracy_score(y_test, y_predict)}
                    决策树模型在训练集上的准确率为：", {metrics.accuracy_score(y_train, dtc.predict(X_train))}
                    {feature},
                    {target}
                            """
                with open(MEDICALMODELINF, 'w') as f :
                    f.write(text)
        
                joblib.dump(dtc,MEDICALMODELPATH)
            elif modeldata['model']=='SVM':
                svr = SVC()
                parameters_SVM = {'kernel' : ['rbf', 'linear'], 'C' : range(4, 5, 6), 'gamma' : [0.1, 0.5, 1]}
        
                grid_SVM = GridSearchCV(svr, parameters_SVM, cv=10)
                grid_SVM.fit(X_train, y_train)
                clf_SVM = grid_SVM.best_estimator_
                clf_SVM.fit(X_train, y_train)
                text=f"""
        支持向量机在训练集上的准确率为： {clf_SVM.score(X_train, y_train)}
        支持向量机在测试集上的准确率为： {clf_SVM.score(X_test, y_test)}
        features : {list(data.columns[:-1])},
        target : {data.columns[-1]}
                """
                if target and feature:
                    text = f"""
        支持向量机在训练集上的准确率为： {clf_SVM.score(X_train, y_train)}
        支持向量机在测试集上的准确率为： {clf_SVM.score(X_test, y_test)}
                    {feature},
                    {target}
                            """
                with open(MEDICALMODELINF, 'w') as f :
                    f.write(text)
        
                joblib.dump(clf_SVM,MEDICALMODELPATH)
            elif modeldata['model'] == 'RandomForestClassifier':
                # 选择分类器的类型
                RF = RandomForestClassifier()

                # 可以通过定义树的各种参数，限制树的大小，防止出现过拟合现象
                parameters = {'n_estimators' : [50, 100, 200],
                              'criterion' : ['entropy', 'gini'],
                              'max_depth' : [4, 5, 6],
                              'min_samples_split' : [2, 4, 6, 8],
                              'min_samples_leaf' : [2, 4, 6, 8, 10]
                              }

                # 自动调参，通过交叉验证确定最优参数。
                grid_obj = GridSearchCV(RF, parameters, cv=10, n_jobs=1)
                grid_obj = grid_obj.fit(X_train, y_train)
    
                clf = grid_obj.best_estimator_
                clf.fit(X_train, y_train)
                predictions = clf.predict(X_test)
                text = f"""
            随机森林模型在测试集上的准确率为: {metrics.accuracy_score(y_test, predictions)}
            随机森林模型在训练集上的准确率为: {metrics.accuracy_score(y_train, clf.predict(X_train))}
            features : {list(data.columns[:-1])},
            target : {data.columns[-1]}
                    """
                if target and feature :
                    text = f"""
            随机森林模型在测试集上的准确率为: {metrics.accuracy_score(y_test, predictions)}
            随机森林模型在训练集上的准确率为: {metrics.accuracy_score(y_train, clf.predict(X_train))}
                            {feature},
                            {target}
                                    """
                with open(MEDICALMODELINF, 'w') as f :
                    f.write(text)
                joblib.dump(clf, MEDICALMODELPATH)
            return 'success'
        except Exception as e:
            return e
    def seeModelMes(self):
        with open(MEDICALMODELINF, 'r') as f :
            return f.read()
