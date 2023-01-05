# 功能窗口大小
FUNC_SIZE=(1200,700)
# 数据库连接
# ip
IPADDRESS='localhost'
#用户名
USERNAME='root'
# 密码
PASSWORD='123'
#数据库
DB='aitrain'
#模型最低r2_score
MINR2=0.75
# 房屋训练数据路径(统一放在data目录下)
HOMEDATANAME='data/HouseProcessed.csv'
#诊断数据路径
MEDICALDATAPATH='data/breast-processed.csv'
#诊断模型信息保存位置
MEDICALMODELINF='./data/medical_model_inf.txt'
#诊断模型路径
MEDICALMODELPATH='model/medical_model.pkl'
#诊断特征值和目标值字段保存位置
MEDICALFEATURESANDTARGET='data/medical_features_target.json'


# 表格宽高
TABLE_W=850
TABLE_H=600

DEGREE=3
# 测试集比例
TEST_SIZE=0.3

ETA0=0.001