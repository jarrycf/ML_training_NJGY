import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import joblib,numpy as np
from utils.dao.stuDataProcess import StuDataProcess


class StuModelTrain:
    def __init__(self):
        self.k_means = joblib.load('model/stuScoreSplit.pkl')
        self.stuDataProcess = StuDataProcess()
        self.getClass()
    def saveModel(self):
        try:
            self.stuDataProcess.outputData()
            data=pd.read_csv('data/output.csv')
            print(data.shape)
            k_means = KMeans(n_clusters=4)
            k_means.fit(data.iloc[:,[1,2]])
            self.k_means=k_means
            joblib.dump(k_means, 'model/stuScoreSplit.pkl')
            return 'train success!'
        except Exception as e:
            return e
    def visSplit(self):
        self.stuDataProcess.outputData()
        data = pd.read_csv('data/output.csv')
        y_predict = self.k_means.predict(data.iloc[:,[1,2]])
        self.getClass()
        plt.subplots(figsize=(10, 5))
        plt.scatter(data.iloc[:,1][y_predict==0],data.iloc[:,2][y_predict==0],label=self.labels[0])
        plt.scatter(data.iloc[:,1][y_predict==1],data.iloc[:,2][y_predict==1],label=self.labels[1])
        plt.scatter(data.iloc[:,1][y_predict==2],data.iloc[:,2][y_predict==2],label=self.labels[2])
        plt.scatter(data.iloc[:,1][y_predict==3],data.iloc[:,2][y_predict==3],label=self.labels[3])
        plt.xlabel('Chinese Score')
        plt.ylabel('Math Score')
        plt.legend(loc='best')
        plt.savefig('images/stu.png')
        cv2.imshow('res',cv2.imread('images/stu.png'))
        cv2.waitKey(0)
    def predict(self):
        self.stuDataProcess.outputData()
        self.getClass()
        data = pd.read_csv('data/output.csv')
        shape=data.shape
        try:
            for i in range(shape[0]) :
                self.stuDataProcess.updateSingleData([data.iloc[:, 0][i], data.iloc[:, 1][i], data.iloc[:, 2][i],self.labels[self.k_means.predict([[data.iloc[:, 1][i],data.iloc[:, 2][i]]])[0]]])
            return 'predict success!'
        except Exception as e:
            return e
    def getClass(self):
        self.labels=[]
        sums=np.sum(self.k_means.cluster_centers_,axis=1)
        for i in self.k_means.cluster_centers_:
            if sum(i)==max(sums):
                self.labels.append('all good')
            elif sum(i)==min(sums):
                self.labels.append('all low')
            elif i[0]<i[1]:
                self.labels.append('low chinese')
            else :
                self.labels.append('low math')
    def singlePre(self,x,y):
        # try:
            return self.labels[self.k_means.predict([[x,y]])[0]]
        # except Exception as e:
        #     return e