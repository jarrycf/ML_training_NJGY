from PyQt5.Qt import *

from frames.widgets.iconButton import IconButton
from utils.homeModelTrain.homeModelTrain import HomeModelTrain
from frames.homeframe.labelFrame import LabelFrame
class TrainModel(QWidget):
    def __init__(self):
        super().__init__()
        self.init_data()
        self.init_ui()
        
    def init_data(self):
        self.homeModelTrain = HomeModelTrain()

    # 初始化控件
    def init_ui(self):
        mainLayout=QGridLayout()
        self.setLayout(mainLayout)
        btnImport=IconButton('训练模型',56)
        btnImport.clicked.connect(self.train_model)
        mainLayout.addWidget(btnImport,1,1)
        btnModelInformation=IconButton('查看模型相关信息',56)
        btnModelInformation.clicked.connect(self.seeModelMes)
        mainLayout.addWidget(btnModelInformation,1,2)
        
        btnPre=IconButton('模型预测',56)
        btnPre.clicked.connect(self.predict)
        mainLayout.addWidget(btnPre,1,3)
    def seeModelMes(self):
        text=self.homeModelTrain.seeModelMes()
        self.label=LabelFrame(text)
        self.label.show()
    def train_model(self):
        res=self.homeModelTrain.saveModel()
        QMessageBox.information(self, "消息提示", str(res))
    def predict(self):
        filename,res=QFileDialog.getOpenFileName(self,'请选择文件','./','*.csv;*.txt;*.xls;*.xlsx')
        res=self.homeModelTrain.predict(filename)
        if res:
            QMessageBox.information(self, "消息提示", str(res))

  
        