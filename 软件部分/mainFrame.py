from PyQt5 import QtGui
from PyQt5.Qt import *
from frames.studentframe import studentFrame
from frames.medicalframe import medicalFrame
from frames.homeframe import homeFrame

class MainFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.init_data()
        self.baseInit()
    # 基础初始化
    def baseInit(self):
        # 设置窗口标题
        self.setWindowTitle("AI实训")
        #设置窗口图标
        self.setWindowIcon(QIcon('favicon.png'))
        # 设置窗口大小
        self.setFixedSize(800, 600)
        #设置窗口背景
        palette = QPalette()
        bac_img=QPixmap("./images/bac.png").scaled(self.size())
        palette.setBrush(QPalette.Background, QBrush(bac_img))
        self.setPalette(palette)
        # 初始化样式
        self.init_qss()
        #初始化控件
        self.init_ui()
        # 显示窗口
        self.show()
    # 初始化数据
    def init_data(self):
        # 初始化字体
        self.font = QtGui.QFont()
        self.font.setFamily("STCaiyun")
    def showStudFrame(self):
        #初始化学生群体划分窗口
        self.studentFrame= studentFrame.StudentFrame()
        self.studentFrame.show()
    def showHomeFrame(self):
        #初始化学生群体划分窗口
        self.homeFrame= homeFrame.HomeFrame()
        self.homeFrame.show()
    def showMedicalFrame(self):
        #初始化学生群体划分窗口
        self.medicalFrame= medicalFrame.MedicalFrame()
        self.medicalFrame.show()
    # 添加控件
    def init_ui(self):
        main_layout=QVBoxLayout()
        main_layout.setContentsMargins(0,130,350,0)
        self.setLayout(main_layout)
        # 第一个功能按钮
        func_button1=QPushButton('学生群体划分')
        func_button1.setObjectName('funcButton')
        func_button1.setFont(self.font)
        func_button1.clicked.connect(self.showStudFrame)
        main_layout.addWidget(func_button1)
        # 第二个功能按钮
        func_button2=QPushButton('房屋价格预测')
        func_button2.setObjectName('funcButton')
        func_button2.setFont(self.font)
        func_button2.clicked.connect(self.showHomeFrame)
        main_layout.addWidget(func_button2)
        # 第三个功能按钮
        func_button3=QPushButton('癌症复发诊断')
        func_button3.setObjectName('funcButton')
        func_button3.clicked.connect(self.showMedicalFrame)
        func_button3.setFont(self.font)
        main_layout.addWidget(func_button3)
        main_layout.addStretch()
    # 初始化样式
    def init_qss(self) :
        with open('qss/pyqt.css','r') as f:
            qApp.setStyleSheet(f.read())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=MainFrame()
    sys.exit(app.exec_())