# 此文档用于ppt截图美化代码 插件名：polacod
#代码
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.cluster import AgglomerativeClustering
from sklearn import svm
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# 1. 读取数据
data = pd.read_csv('./data/Score_train.csv')

# 2. 数据预处理：pca降维
# transfer = PCA(n_components=0.95)
# data_new = transfer.fit_transform(data)

# 3. 选择模型
estimator = KMeans(n_clusters=4)
estimator.fit(data)

y_predict = estimator.predict(data)
y_predict[:300]
silhouette_score(data, y_predict)
print('聚类的轮廓系数为:{}'.format( \
    silhouette_score(data, y_predict)))


# 1. 读取数据
data = pd.read_csv('./data/Score_train.csv')

estimator = AgglomerativeClustering(
    n_clusters=4, affinity='euclidean', linkage='ward')
estimator.fit(data)
silhouette_score(data, estimator.labels_)

clf = svm.SVC()
clf.fit(data, estimator.labels_)

clf.feature_importances_

from sklearn.ensemble import ExtraTreesClassifier
clf = ExtraTreesClassifier()
clf.fit(train_x, train_y.astype(int))
clf.feature_importances_


param_4={'C':[1, 2, 4], 'penalty':['l1', 'l2']}
model_4=GridSearchCV(estimator = LogisticRegression(), param_grid = param_4, n_jobs=1, cv=5)
model_4.fit(x_train,y_train.astype(int))

param_5 = {'n_estimators':list(range(100, 600, 50))}
model_5 = GridSearchCV(estimator = GradientBoostingClassifier(), param_grid = param_5, n_jobs=-1, cv=5)
model_5.fit(x_train,y_train.astype(int))

param_6={'gamma':np.linspace(0, 0.001, 100)}
model_6=GridSearchCV(estimator = SVC(kernel = 'rbf'), param_grid = param_6, n_jobs=-1,cv=5)
model_6.fit(x_train,y_train.astype(int))

param_3={'n_neighbors':[i for i in range(1,11)], 'p':[i for i in range(1,6)]} 
model_3=GridSearchCV(estimator = neighbors.KNeighborsClassifier(), param_grid = param_3, n_jobs=-1, cv=5)
model_3.fit(x_train,y_train.astype(int))