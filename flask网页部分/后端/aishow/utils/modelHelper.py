import joblib
import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler, LabelEncoder


class ModelHelper:
    def __init__(self):
        self.stuModel=joblib.load('aishow/model/stuScoreSplit.pkl')
        self.homeModel=joblib.load('aishow/model/housePricePre.pkl')
        self.medicalModel=joblib.load('aishow/model/medical_model.pkl')
        self.getClass()
    def getClass(self):
        self.stuLabels=[]
        sums=np.sum(self.stuModel.cluster_centers_,axis=1)
        for i in self.stuModel.cluster_centers_:
            if sum(i)==max(sums):
                self.stuLabels.append('all good')
            elif sum(i)==min(sums):
                self.stuLabels.append('all low')
            elif i[0]<i[1]:
                self.stuLabels.append('low chinese')
            else :
                self.stuLabels.append('low math')
    def predictStu(self,a,b):
        return self.stuLabels[self.stuModel.predict([[a,b]])[0]]
    def predictHome(self,a,b,c):
        polyfit = PolynomialFeatures(degree=3)
        feature = polyfit.fit_transform([[a,b,c]])
        return    self.homeModel.predict(feature)[0]
    def predictMedical(self,a,b,c,d,e,f,g,h):
        print(a,b,c,d,e,f,g,h)
        lb = LabelEncoder()
        lb.fit(['10-19', '20-29', '30-39','40-49','50-59','60-69','70-79', '80-89','90-99'])
        a=lb.transform([a])[0]
        
        lb.fit(['lt40', 'ge40', 'premeno'])
        b=lb.transform([b])[0]
        
        lb.fit(['0-4', '5-9', '10-14', '15-19', '20-24', '25-29','30-34','35-39', '40-44','45-49', '50-54', '55-59'])
        c=lb.transform([c])[0]
        lb.fit(['0-2', '3-5', '6-8','9-11', '12-14', '15-17', '18-20', '21-23','24-26', '27-29', '30-32', '33-35','36-39'])
        d=lb.transform([d])[0]
        
        lb.fit(['yes', 'no'])
        e=lb.transform([e])[0]
        
        # lb.fit(['1', '2','3'])
        # f=lb.transform([f])[0]
        lb.fit(['left_up', 'left_low', 'right_up', 'right_low', "central"])
        g=lb.transform([g])[0]
        
        lb.fit(['yes','no'])
        h=lb.transform([h])[0]
        pre=self.medicalModel.predict([[a,b,c,d,e,f,g,h]])
        return pre[0]
        
model=ModelHelper()
# print(model.predictHome(32,84.87882,10,24.98298,121.54024,37.9))