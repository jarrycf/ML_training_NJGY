# -*- coding:utf-8 -*-
import os
import random
import sys

import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QTableWidget, QHBoxLayout, QTableWidgetItem, QComboBox, \
    QFrame, QMenu, QMessageBox
from PyQt5.QtGui import QFont, QColor, QBrush, QPixmap, QIcon, QCursor
from utils.dao.stuDataProcess import StuDataProcess
from frames.studentframe.QMyTable import QMyTable
class TableSheet(QWidget) :
    def __init__(self) :
        super().__init__()
        self.stuDataProcess=StuDataProcess()
        self.initUi()
    def initUi(self) :
        self.setFixedSize(1200,500)
        self.table = QTableWidget()  # 也可以QTableWidget(5,2)
        self.table.setAlternatingRowColors(True)
        self.table.setContextMenuPolicy(
            Qt.CustomContextMenu)  # 右键菜单，如果不设为CustomContextMenu,无法使用customContextMenuRequested
        self.table.customContextMenuRequested.connect(self.showContextMenu)
        for index in range(self.table.columnCount()) :
            headItem = self.table.horizontalHeaderItem(index)
            headItem.setFont(QFont("song", 12, QFont.Bold))
            headItem.setForeground(QBrush(Qt.gray))
            headItem.setTextAlignment(0x000 | Qt.AlignHCenter)
     
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.table)
        self.setLayout(mainLayout)
    def initData(self,data):
        headers=list(data.columns)
        self.table.setColumnCount(len(headers))  #
        self.table.setRowCount(len(data))  #
        # 隐藏垂直的表头，self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(headers)
        self.setFixedSize(len(headers)*300,self.height())
        for i in  range(len(headers)):
            self.table.setColumnWidth(i,300)
        for index in range(self.table.columnCount()) :
            headItem = self.table.horizontalHeaderItem(index)
            headItem.setFont(QFont("song", 13, QFont.Bold))
            headItem.setForeground(QBrush(Qt.gray))
            headItem.setTextAlignment(Qt.AlignCenter)
        for i in range(len(data)):
            for headerindex in range(len(headers)):
                newItem=QTableWidgetItem(str(data.iloc[i,headerindex]))
                newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.table.setItem(i, headerindex,newItem)

    def showFull(self):
        self.stuDataProcess.outputData()
        self.initData(pd.read_csv('data/output.csv'))
    def showContextMenu(self, pos) :  # 创建右键菜单
        self.table.contextMenu = QMenu(self)
        lis = os.listdir('images/icons')
        self.actionDeleteRow = self.table.contextMenu.addAction(QIcon(os.path.join('images/icons', random.choice(lis))),
                                                                '删除行')
        self.actionDeleteRow.triggered.connect(self.deleteRow)
    
    
        actionStandProcess = self.table.contextMenu.addAction(
            QIcon(os.path.join('images/icons', random.choice(lis))), 'all good')
        actionStandProcess.triggered.connect(lambda :self.selectSingleClass('all good'))
    
        actionStandProcess = self.table.contextMenu.addAction(
            QIcon(os.path.join('images/icons', random.choice(lis))), 'all low')
        actionStandProcess.triggered.connect(lambda :self.selectSingleClass('all low'))
        
        actionStandProcess = self.table.contextMenu.addAction(
            QIcon(os.path.join('images/icons', random.choice(lis))), 'low chinese')
        actionStandProcess.triggered.connect(lambda :self.selectSingleClass('low chinese'))
        
        actionStandProcess = self.table.contextMenu.addAction(
            QIcon(os.path.join('images/icons', random.choice(lis))), 'low math')
        actionStandProcess.triggered.connect(lambda :self.selectSingleClass('low math'))

        actionStandProcess = self.table.contextMenu.addAction(
            QIcon(os.path.join('images/icons', random.choice(lis))), '显示全部')
        actionStandProcess.triggered.connect(self.showFull)
    
    
    
        self.table.contextMenu.popup(QCursor.pos())  # 2菜单显示的位置
        self.table.contextMenu.show()
    def selectSingleClass(self,classType):
        try:
            self.stuDataProcess.outputData()
            data = pd.read_csv('data/output.csv')
            self.initData(data[data['类别'] == classType])
            self.table.show()
        except Exception as e:
            QMessageBox.information(self,'Message',str(e),QMessageBox.Ok)
    def deleteRow(self) :
        s_items = self.table.selectedItems()
        if s_items :
            selected_rows = []  # 求出所选择的行数
            for i in s_items :
                row = i.row()
                if row not in selected_rows :
                    selected_rows.append(row)
            for r in range(len(sorted(selected_rows))) :
                item=self.table.item(selected_rows[r],0)
                if item:
                    print(item.text())
                    self.stuDataProcess.removeRow(int(item.text()))
                    self.table.removeRow(selected_rows[r] - r)  # 删除行


        

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    table = TableSheet()
    table.setWindowTitle('TableWidget Usage')
    table.resize(700, 300)
    table.show()
    sys.exit(app.exec_())