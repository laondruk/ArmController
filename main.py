from PyQt5 import QtWidgets    #PyQt5 호출
import sys

class window(QtWidgets.QWidget):   #window 창 설정

    def __init__(self):
        super(window,self).__init__()
        self.setGeometry(300, 300, 320, 240)   #window 크기
        self.setWindowTitle('ArmController')   #window 명칭
        self.show()                            #window 창 실행

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    app.exec_()
