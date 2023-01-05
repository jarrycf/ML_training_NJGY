from PyQt5.Qt import QLabel

class LabelFrame(QLabel):
    def __init__(self,label):
        super().__init__()
        self.setWindowTitle('模型信息')
        self.setStyleSheet('font-size:30px')
        self.setText(label)

    