import json

from PyQt5.Qt import *

from frames.widgets.iconButton import IconButton
from utils.homeModelTrain.homeModelTrain import HomeModelTrain
class SelectModel(QWidget):
    def __init__(self):
        super().__init__()
        self.init_data()
        self.init_ui()
        
    def init_data(self):
        self.homeModelTrain=HomeModelTrain()

    # 初始化控件
    def init_ui(self):
        mainLayout=QGridLayout()
        self.setLayout(mainLayout)
        btnImport=IconButton('LinearModel',56)
        btnImport.clicked.connect(lambda :self.selectModel('linerModel'))
        mainLayout.addWidget(btnImport,1,1)
        
        btnReg=IconButton('Ridge',56)
        btnReg.clicked.connect(lambda :self.selectModel('Ridge'))
        mainLayout.addWidget(btnReg,1,2)
        
        btnReg=IconButton('SGDRegressor',56)
        btnReg.clicked.connect(lambda :self.selectModel('SGDRegressor'))
        mainLayout.addWidget(btnReg,1,3)
        

        


    def selectModel(self,model):
        try :
            with open('data/select_model.json', 'r') as f :
                data = json.loads(f.read())
                data['model'] = model
            with open('data/select_model.json', 'w') as f :
                f.write(json.dumps(data))
            QMessageBox.information(self, "消息提示",  'select model success!')

        except Exception as e :
            QMessageBox.information(self, "消息提示", str(e))


    
        