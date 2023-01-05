import json

from PyQt5.Qt import *

from frames.widgets.iconButton import IconButton
from utils.medicalModelTrain.medicalModelTrain import MedicalModelTrain
class SelectModel(QWidget):
    def __init__(self):
        super().__init__()
        self.init_data()
        self.init_ui()
        
    def init_data(self):
        self.medicalModelTrain=MedicalModelTrain()

    # 初始化控件
    def init_ui(self):
        mainLayout=QGridLayout()
        self.setLayout(mainLayout)
        btnImport=IconButton('SVM',56)
        btnImport.clicked.connect(lambda :self.selectModel('SVM'))
        mainLayout.addWidget(btnImport,1,1)
        
        
        btnImport=IconButton('DecisionTreeClassifier',56)
        btnImport.clicked.connect(lambda :self.selectModel('DecisionTreeClassifier'))
        mainLayout.addWidget(btnImport,1,2)
        
        btnImport=IconButton('RandomForestClassifier',56)
        btnImport.clicked.connect(lambda :self.selectModel('RandomForestClassifier'))
        mainLayout.addWidget(btnImport,1,3)
        


        
      

    def selectModel(self,model):
        try :
            with open('data/select_model2.json', 'r') as f :
                data = json.loads(f.read())
                data['model'] = model
            with open('data/select_model2.json', 'w') as f :
                f.write(json.dumps(data))
            QMessageBox.information(self, "消息提示",  'select model success!')

        except Exception as e :
            QMessageBox.information(self, "消息提示", str(e))


    
        