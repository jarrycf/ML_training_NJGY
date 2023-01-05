# -*- coding:utf-8 -*-
import os
import random

import cv2 as cv
import sys
import seaborn as sns
import pandas as pd
from PyQt5.Qt import *
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from config.config import TABLE_H,TABLE_W
class TableSheet(QWidget) :
    def __init__(self) :
        super().__init__()
        self.initUi()
        self.initData(pd.read_csv('data/HouseProcessed.csv'))
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
            df.to_csv('data/HouseProcessed.csv', index=False)
            return 'success!'
        except Exception as e:
            return e

    def showContextMenu(self, pos) :  # 创建右键菜单
        self.table.contextMenu = QMenu(self)
        lis=os.listdir('images/icons')

        self.actionDeleteRow=self.table.contextMenu.addAction(QIcon(os.path.join('images/icons',random.choice(lis))),'删除行')
        self.actionDeleteRow.triggered.connect(self.deleteRow )
        
        self.actionDeleteCol= self.table.contextMenu.addAction(QIcon(os.path.join('images/icons',random.choice(lis))),'删除列')
        self.actionDeleteCol.triggered.connect(self.deleteColumn )
        
        self.actionStandProcess=self.table.contextMenu.addAction(QIcon(os.path.join('images/icons',random.choice(lis))),'归一化处理')
        self.actionStandProcess.triggered.connect(self.standProcess )
        
        self.actionCorr= self.table.contextMenu.addAction(QIcon(os.path.join('images/icons',random.choice(lis))),'数据相关性')
        self.actionCorr.triggered.connect(self.showCorr )
        
        self.actionScatter=self.table.contextMenu.addAction(QIcon(os.path.join('images/icons',random.choice(lis))),'散点图绘制')
        self.actionScatter.triggered.connect(self.showScatter )
        
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
            for col in selected_cols :
                lis=[]
                for row in range(self.table.rowCount()) :
                    lis.append(eval(self.table.item(row,col).text()))
                # maxV=max(lis)
                # minV=min(lis)
                transfer = StandardScaler()
                x_train = transfer.fit_transform([lis])
                for row in range(self.table.rowCount()) :
                    # self.table.item(row, col).setText(str((lis[row]-minV)/maxV))
                    self.table.item(row, col).setText(str(x_train[0][row]))

    def showCorr(self):
        self.exportToCsv()
        data=pd.read_csv('data/HouseProcessed.csv')
        corr = data.corr()
        plt.subplots(figsize=(12, 9))
        sns.heatmap(corr,fmt='.2f', vmax=0.9, square=True, linecolor='white')
        plt.savefig('images/corr.png')
        cv.imshow('corr',cv.imread('images/corr.png'))
        cv.waitKey(0)
    def showScatter(self):
        s_items = self.table.selectedItems()
        if s_items :
            selected_cols = []  # 求出所选择的列数
            for i in s_items :
                col = i.column()
                if col not in selected_cols :
                    selected_cols.append(col)
            self.exportToCsv()
            data = pd.read_csv('data/HouseProcessed.csv')
            for i in selected_cols:
                plt.subplots(figsize=(10, 5))
                plt.scatter(data.iloc[:,i],data.iloc[:,-1])
                plt.xlabel(data.columns[i])
                plt.ylabel(data.columns[-1])
                plt.savefig('images/scatter.png')
                cv.imshow(f"scatter{i}",cv.imread('images/scatter.png'))
            cv.waitKey(0)
       
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    table = TableSheet()
    table.setWindowTitle('TableWidget Usage')
    table.resize(700, 300)
    table.show()
    sys.exit(app.exec_())