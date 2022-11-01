import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class window(QWidget):   #window 창 설정

    def __init__(self):
        super(window,self).__init__()
        self.setGeometry(300, 300, 1920, 1080)   #window 크기
        self.setWindowTitle('ArmController')   #window 명칭               
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("BTN", self)
        btn1.move(960, 540)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = window()
    win.show()
    app.exec_()
