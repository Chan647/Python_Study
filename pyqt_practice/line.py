import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt

form_class = uic.loadUiType("line.ui")[0]

class Window(QMainWindow, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.lineEdit.setText("Push")
        # print(self.lineEdit.text())
        self.lineEdit.setPlaceholderText("여기에 입력하세요")


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()