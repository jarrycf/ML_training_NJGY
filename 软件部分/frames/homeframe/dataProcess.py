import pandas as pd
from PyQt5.Qt import *

from frames.widgets.iconButton import IconButton
from utils.dao.homeDataProcess import HomeDataProcess
from frames.homeframe.tableFrame import TableSheet
class DataProcess(QWidget):
    def __init__(self):
        super().__init__()
        self.init_data()
        self.init_ui()
        
    def init_data(self):
        self.homeDataProcess = HomeDataProcess()
        self.tableSheet=TableSheet()
    # 导入数据
    def import_data(self):
        filename,res=QFileDialog.getOpenFileName(self,'请选择文件','./','*.csv;*.txt;*.xls;*.xlsx')
        if res:
            data=pd.read_csv(filename)
            self.tableSheet.initData(data)
    #导出数据
    def output_data(self):
        res=self.tableSheet.exportToCsv()
        QMessageBox.information(self, "消息提示", str(res))
    def init_ui(self):
        mainLayout=QHBoxLayout()
        self.setLayout(mainLayout)
        leftLayout=QVBoxLayout()
        mainLayout.addLayout(leftLayout)
        btnImport=IconButton('导入数据',56)
        btnImport.clicked.connect(self.import_data)
        leftLayout.addWidget(btnImport)
        btnOutput=IconButton('导出数据',56)
        btnOutput.clicked.connect(self.output_data)
        leftLayout.addWidget(btnOutput)
        mainLayout.addWidget(self.tableSheet)
        
 