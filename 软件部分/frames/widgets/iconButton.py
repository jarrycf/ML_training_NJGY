import os

from PyQt5.Qt import QToolButton,QIcon
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication
import random

class IconButton(QToolButton):
    def __init__(self,text,index=13):
        super(IconButton, self).__init__()
        # icon = QApplication.style().standardIcon(random.randint(0,69))
        self.setStyleSheet('background-color:transparent;font-size:20px;')
        self.setText(text)
        self.setIconSize(QSize(80,80))
        self.setIcon(QIcon(os.path.join('images/icons',random.choice(os.listdir('images/icons')))))
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

    def enterEvent(self, e) :  # 鼠标移入label
        self.setStyleSheet('background-color:transparent;font-size:20px;color:red;')

    def leaveEvent(self, e) :  # 鼠标离开label
        self.setStyleSheet('background-color:transparent;font-size:20px;color:black;')