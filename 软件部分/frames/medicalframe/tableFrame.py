# -*- coding:utf-8 -*-
import json
import os
import random
from config.config import TABLE_H,TABLE_W


import sys

import pandas as pd
from PyQt5.Qt import *

from sklearn.preprocessing import LabelEncoder

class TableSheet(QWidget) :
    def __init__(self) :
        super().__init__()
        self.initUi()
        self.initData(pd.read_csv('data/breast-processed.csv'))
        self.predictDict = {
            'age' : ['10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-99'],
            'menopause' : ['lt40', 'ge40', 'premeno'],
            'tumor-size' : ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49',
                            '50-54', '55-59'],
            'inv-nodes' : ['0-2', '3-5', '6-8', '9-11', '12-14', '15-17', '18-20', '21-23', '24-26', '27-29', '30-32',
                           '33-35', '36-39'],
            'node-caps' : ['yes', 'no'],
            'deg-malig' : ['1', '2', '3'],
            'breast-quad' : ['left_up', 'left_low', 'right_up', 'right_low', "central"],
            'irradiat' : ['yes', 'no'],
    'Class':['no-recurrence-events','recurrence-events']
        }
        if not os.path.exists('data/trainData.txt'):
            self.trainData = {
                'labelEncoder' : [],
                'target' : '',
            }
        else:
            with open('data/trainData.txt','r') as f:
                self.trainData=json.loads(f.read())

    def table_change(self, index):
        row = index.row()
        print(row)
    def initUi(self) :
        self.setFixedSize(TABLE_W,TABLE_H)
        self.table = QTableWidget()
        self.table.setAlternatingRowColors(True)
        self.table.setContextMenuPolicy(
            Qt.CustomContextMenu)  # 右键菜单，如果不设为CustomContextMenu,无法使用customContextMenuRequested
        self.table.customContextMenuRequested.connect(self.showContextMenu)
        self.table.doubleClicked.connect(self.table_change)
        # self.table.setSelectionBehavior(QTableWidget.SelectColumns)
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
        for i in  range(len(headers)):
            self.table.setColumnWidth(i, 300)
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

    def exportToCsv(self) :
        try:
            columnHeaders = []
            for j in range(self.table.columnCount()) :
                columnHeaders.append(self.table.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)
        
            for row in range(self.table.rowCount()) :
                for col in range(self.table.columnCount()) :
                    item = self.table.item(row, col)
                    df.at[row, columnHeaders[col]] = item.text() if item is not None else ""
            df.to_csv('data/breast-processed.csv', index=False)
            with open('data/trainData.txt', 'w') as f :
                f.write(json.dumps(self.trainData))
            return 'success!'
        except Exception as e:
            return e
    def selectTartget(self):
        try:
            s_items = self.table.selectedItems()
            if s_items :
                selected_cols = []  # 求出所选择的列数
                for i in s_items :
                    col = i.column()
                    if col not in selected_cols :
                        selected_cols.append(col)
                self.trainData['target']=self.table.horizontalHeaderItem(selected_cols[0]).text()
                QMessageBox.information(self,'information',f'set success {self.trainData["target"]} !',QMessageBox.Ok)
        except Exception as e:
            QMessageBox.information(self, 'information', str(e), QMessageBox.Ok)

    def showContextMenu(self, pos) :  # 创建右键菜单
        self.table.contextMenu = QMenu(self)
        lis=os.listdir('images/icons')
        self.actionDeleteRow= self.table.contextMenu.addAction(QIcon(os.path.join('images/icons',random.choice(lis))),'删除行')
        self.actionDeleteRow.triggered.connect(self.deleteRow )
        
        self.actionDeleteCol=self.table.contextMenu.addAction(QIcon(os.path.join('images/icons',random.choice(lis))),'删除列')
        self.actionDeleteCol.triggered.connect(self.deleteColumn )
        
        self.actionStandProcess= self.table.contextMenu.addAction(QIcon(os.path.join('images/icons',random.choice(lis))),'LabelEncoder')
        self.actionStandProcess.triggered.connect(self.standProcess )
        
        self.actionSelectTarget= self.table.contextMenu.addAction(QIcon(os.path.join('images/icons',random.choice(lis))),'设为目标值')
        self.actionSelectTarget.triggered.connect(self.selectTartget )
        
        self.table.contextMenu.popup(QCursor.pos())  # 2菜单显示的位置
        self.table.contextMenu.show()
    def deleteRow(self):
        s_items = self.table.selectedItems()
        if s_items :
            selected_rows = []  # 求出所选择的行数
            for i in s_items :
                row = i.row()
                if row not in selected_rows :
                    selected_rows.append(row)
            for r in range(len(sorted(selected_rows))) :
                self.table.removeRow(selected_rows[r] - r)  # 删除行
    
    def deleteColumn(self):
        s_items = self.table.selectedItems()
        if s_items :
            selected_cols = []  # 求出所选择的列数
            for i in s_items :
                col = i.column()
                if col not in selected_cols :
                    selected_cols.append(col)
            for r in range(len(sorted(selected_cols))) :
                self.table.removeColumn(selected_cols[r] - r)
                
                
    def  standProcess(self):
        s_items = self.table.selectedItems()
        if s_items :
            selected_cols = []  # 求出所选择的列数
            for i in s_items :
                col = i.column()
                if col not in selected_cols :
                    selected_cols.append(col)
            self.exportToCsv()
            data=pd.read_csv('data/breast-processed.csv')
            for col in selected_cols :
                print(data.columns[col])
                transfer = LabelEncoder()
                transfer.fit(self.predictDict[data.columns[col]])
                x_train = transfer.transform(data.iloc[:,col])
                try:
                    for row in range(self.table.rowCount()) :
                        self.table.item(row, col).setText(str(x_train[row]))
                except Exception as e:
                    QMessageBox.information(self,'消息提示',str(e),QMessageBox.Ok)
                for i in selected_cols:
                    self.trainData['labelEncoder'].append(self.table.horizontalHeaderItem(i).text())
                self.trainData['labelEncoder']=list(set(self.trainData['labelEncoder']))


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    table = TableSheet()
    table.setWindowTitle('TableWidget Usage')
    table.resize(700, 300)
    table.show()
    sys.exit(app.exec_())