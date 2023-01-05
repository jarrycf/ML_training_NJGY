from autogluon.tabular import TabularDataset, TabularPredictor
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_csv('./data/House_Training_index.csv')
train_data, test_data = train_test_split(data,
                                         test_size=0.2, random_state=0)

#训练
train_data = TabularDataset(train_data)
id, label = 'index', 'Y house price of unit area'

# 数据预处理
large_val_cols = ['X1 transaction date', 'X2 house age',
                  'X3 distance to the nearest MRT station',
                  'X4 number of convenience stores',
                  'X5 latitude',
                  'X6 longitude']
for c in large_val_cols + [label]:
    train_data[c] = np.log(train_data[c] + 1)
predictor = TabularPredictor(label=label).fit(train_data.drop(columns=[id]))

#预测
test_data = TabularDataset(test_data）
preds=predictor.predict(test_data.drop(columns=[id])）
submission=pd.DataFrame(
    {id: test_datal[id], label: preds})
submission.to_csv(
    'submission.csv', index=False)
