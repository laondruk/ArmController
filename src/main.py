import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class window(QWidget):   #window â ����

    def __init__(self):
        super(window,self).__init__()
        self.setGeometry(300, 300, 1920, 1080)   #window ũ��
        self.setWindowTitle('ArmController')   #window ��Ī               
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("BTN", self)
        btn1.move(960, 540)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = window()
    win.show()
    app.exec_()
