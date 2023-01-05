import pandas as pd
from PyQt5.Qt import *
from utils.dao.stuDataProcess import StuDataProcess
from frames.widgets.iconButton import IconButton
from utils.stuModelTrain.stuModelTrain import StuModelTrain
from frames.studentframe.tableFrame import TableSheet
class DataProcess(QWidget):
    def __init__(self):
        super().__init__()
        self.init_data()
        self.init_ui()
        
    def init_data(self):
        self.stuDataProcess = StuDataProcess()
        self.stuModelTrain=StuModelTrain()
    # 导入数据
    def import_data(self):
        filename=QFileDialog.getOpenFileName(self,'请选择文件','./','*.csv;*.txt;*.xls;*.xlsx')
        res=self.stuDataProcess.insertData(filename[0])
        QMessageBox.information(self, "消息提示", str(res))
    #删除数据
    def delete_data(self):
        res=self.stuDataProcess.deleteData()
        QMessageBox.information(self, "消息提示", str(res))
    #导出数据
    def output_data(self):
        res=self.stuDataProcess.outputData()
        QMessageBox.information(self, "消息提示", str(res))
    def show_data(self):
        self.stuDataProcess.outputData()
        self.table=TableSheet()
        self.table.initData(pd.read_csv('data/output.csv'))
        self.table.show()
    # 初始化控件
    def init_ui(self):
        mainLayout=QGridLayout()
        self.setLayout(mainLayout)
        btnImport=IconButton('添加数据',56)
        btnImport.clicked.connect(self.addRow)
        mainLayout.addWidget(btnImport,1,1)
        
        btnOutput=IconButton('批量添加',31)
        btnOutput.clicked.connect(self.import_data)
        mainLayout.addWidget(btnOutput,1,2)
        
        btnShow=IconButton('查看数据',36)
        btnShow.clicked.connect(self.show_data)
        mainLayout.addWidget(btnShow,2,1)
        
        btnClear=IconButton('清空数据',14)
        btnClear.clicked.connect(self.delete_data)
        mainLayout.addWidget(btnClear,2,2)
        
        btnSearch=IconButton('学号查询',35)
        btnSearch.clicked.connect(self.selectSno)
        mainLayout.addWidget(btnSearch,1,3)
        
        btnAdd=IconButton('全部预测',41)
        btnAdd.clicked.connect(self.pre_model)
        mainLayout.addWidget(btnAdd,2,3)
    def selectSno(self):
        r1, ok1 = QInputDialog.getInt(self, '学号查询', '请输入学生学号：',value=2111,step=10)
        if ok1:
            res= self.stuDataProcess.selectSno(r1)
            if res:
                QMessageBox.information(self, "消息提示", res)
            else:
                QMessageBox.information(self, "消息提示", '该学号不存在!')

    def pre_model(self):

        res=self.stuModelTrain.predict()
        if res:
            QMessageBox.information(self, "消息提示", str(res))
    def addRow(self):
        r1, ok1 = QInputDialog.getInt(self, '学号', '请输入学生学号：',value=2111,step=10)
        if ok1:
            r2, ok2 = QInputDialog.getInt(self, '语文成绩', '请输入语文成绩：',value=50,step=2,min=0,max=100)
            if ok2:
                r3, ok3 = QInputDialog.getInt(self, '数学成绩', '请输入数学成绩：',value=50,step=2,min=0,max=100)
                res=self.stuDataProcess.insertRow(r1,r2,r3)
                QMessageBox.information(self, "消息提示", str(res))
                return
        QMessageBox.information(self, "消息提示", '退出成功!')


    
        