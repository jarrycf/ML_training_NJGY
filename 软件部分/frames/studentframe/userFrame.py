from PyQt5.Qt import *
from utils.dao.stuDataProcess import StuDataProcess
from frames.widgets.iconButton import IconButton


class UserFrame(QWidget) :
    def __init__(self) :
        super().__init__()
        self.init_data()
        self.init_ui()
    
    def init_data(self) :
        self.stuDataProcess = StuDataProcess()
    
    # 导入数据
    def import_data(self) :
        filename = QFileDialog.getOpenFileName(self, '请选择文件', './', '*.csv;*.txt;*.xls;*.xlsx')
        res = self.stuDataProcess.insertData(filename[0])
        QMessageBox.information(self, "消息提示", str(res))
    
    # 删除数据
    def delete_data(self) :
        res = self.stuDataProcess.deleteData()
        QMessageBox.information(self, "消息提示", str(res))
    
    # 导出数据
    def output_data(self) :
        res = self.stuDataProcess.outputData()
        QMessageBox.information(self, "消息提示", str(res))
    
    def show_data(self) :
        res = self.stuDataProcess.showData()
        if res :
            QMessageBox.information(self, "消息提示", str(res))
    
    # 初始化控件
    def init_ui(self) :
        mainLayout = QGridLayout()
        self.setLayout(mainLayout)
        btnImport = IconButton('导入数据', 56)
        btnImport.clicked.connect(self.import_data)
        mainLayout.addWidget(btnImport, 1, 1)
        
        btnOutput = IconButton('导出数据', 31)
        btnOutput.clicked.connect(self.output_data)
        mainLayout.addWidget(btnOutput, 1, 2)
        
        btnShow = IconButton('查看数据', 36)
        btnShow.clicked.connect(self.show_data)
        mainLayout.addWidget(btnShow, 2, 1)
        
        btnClear = IconButton('清空数据', 14)
        btnClear.clicked.connect(self.delete_data)
        mainLayout.addWidget(btnClear, 2, 2)
        
        btnSearch = IconButton('获取数据', 35)
        btnSearch.clicked.connect(lambda : webbrowser.open('https://www.bilibili.com/'))
        mainLayout.addWidget(btnSearch, 1, 3)
        
        btnAdd = IconButton('扫码关注', 41)
        mainLayout.addWidget(btnAdd, 2, 3)


