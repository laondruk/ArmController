from PyQt5 import QtWidgets    #PyQt5 ȣ��
import sys

class window(QtWidgets.QWidget):   #window â ����

    def __init__(self):
        super(window,self).__init__()
        self.setGeometry(300, 300, 320, 240)   #window ũ��
        self.setWindowTitle('ArmController')   #window ��Ī
        self.show()                            #window â ����

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    app.exec_()
