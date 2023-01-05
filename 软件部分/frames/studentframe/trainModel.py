from PyQt5.Qt import *

from frames.widgets.iconButton import IconButton
from utils.dao.stuDataProcess import StuDataProcess
from utils.stuModelTrain.stuModelTrain import StuModelTrain
class TrainModel(QWidget):
    def __init__(self):
        super().__init__()
        self.init_data()
        self.init_ui()
        
    def init_data(self):
        self.stuDataProcess = StuDataProcess()
        self.stuModelTrain=StuModelTrain()

    # 初始化控件
    def init_ui(self):
        mainLayout=QGridLayout()
        self.setLayout(mainLayout)
        btnImport=IconButton('训练模型',56)
        btnImport.clicked.connect(self.train_model)
        mainLayout.addWidget(btnImport,1,1)
        btnVis=IconButton('可视化模型',56)
        btnVis.clicked.connect(self.vis_model)
        mainLayout.addWidget(btnVis,1,2)
    def train_model(self):
        res=self.stuModelTrain.saveModel()
        QMessageBox.information(self, "消息提示", str(res))
    def vis_model(self):
        self.stuModelTrain.visSplit()

   