from PyQt5.Qt import *
from config.config import *
from frames.studentframe import dataProcess,trainModel,preModel
from frames.widgets.iconButton import IconButton


class StudentFrame(QMainWindow):
    def __init__(self, parent=None) :
        super(StudentFrame, self).__init__(parent)
        # 初始化数据
        self.init_data()
        # 设置窗口标题
        self.setWindowTitle("学生群体划分")
        #设置窗口图标
        self.setWindowIcon(QIcon('favicon.png'))
        # 设置窗口大小
        self.resize(FUNC_SIZE[0], FUNC_SIZE[1])
        # 设置窗口背景
        palette = QPalette()
        bac_img = QPixmap("./images/funcbac.jpg").scaled(self.width(), self.height() + 500)
        palette.setBrush(QPalette.Background, QBrush(bac_img))
        self.setPalette(palette)
        self.init_ui()
    def init_data(self):
        ...
    def init_ui(self):
        toolBar = QToolBar(self)
        self.addToolBar(Qt.LeftToolBarArea, toolBar)
        btnImport = IconButton('数据处理')
        btnImport.clicked.connect(lambda :self.onButtonClicked(0))
        toolBar.addWidget(btnImport)
        btnTrain= IconButton('训练模型')
        btnTrain.clicked.connect(lambda :self.onButtonClicked(1))
        toolBar.addWidget(btnTrain)
        btnPredict= IconButton('测试模型')
        btnPredict.clicked.connect(lambda :self.onButtonClicked(2))
        toolBar.addWidget(btnPredict)
        # 添加主布局
        mainWidget = QWidget(self)
        self.mainLayout = QStackedLayout(mainWidget)
        self.mainLayout.addWidget(dataProcess.DataProcess())
        self.mainLayout.addWidget(trainModel.TrainModel())
        self.mainLayout.addWidget(preModel.PreModel())
        mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(mainWidget)
   
    def onButtonClicked(self, index):
        if index < self.mainLayout.count():
            self.mainLayout.setCurrentIndex(index)