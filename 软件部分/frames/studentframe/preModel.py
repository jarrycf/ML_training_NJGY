from PyQt5.Qt import *

from frames.studentframe.dataProcess import DataProcess
from frames.widgets.iconButton import IconButton
from utils.dao.stuDataProcess import StuDataProcess
from utils.stuModelTrain.stuModelTrain import StuModelTrain
class PreModel(QWidget):
    def __init__(self):
        super().__init__()
        self.init_data()
        self.init_ui()
        
    def init_data(self):
        self.stuDataProcess = DataProcess()
        self.stuModelTrain=StuModelTrain()

    # 初始化控件
    def init_ui(self):
        mainLayout=QGridLayout()
        self.setLayout(mainLayout)
        btnImport=IconButton('全部预测',56)
        btnImport.clicked.connect(self.pre_model)
        mainLayout.addWidget(btnImport,1,1)
        
        btnSingle=IconButton('单一预测',56)
        btnSingle.clicked.connect(self.single_pre)
        mainLayout.addWidget(btnSingle,1,2)
    def pre_model(self):
        res=self.stuModelTrain.predict()
        self.stuDataProcess.show_data()
    def single_pre(self):
        c, ok = QInputDialog.getInt(self, '语文成绩', '请输入语文成绩：')
        m, ok2 = QInputDialog.getInt(self, '数学成绩', '请输入数学成绩：')
        res=self.stuModelTrain.singlePre(c,m)
        QMessageBox.information(self, "消息提示", str(res))
   
    
        