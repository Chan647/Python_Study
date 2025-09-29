import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt

form_class = uic.loadUiType("text.ui")[0]

class Window(QMainWindow, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.textEdit.setPlainText("여기에 입력하세요")
        # print(self.textEdit.toPlainText())
        self.pushButton.clicked.connect(self.func)
    
    def func(self) :
        self.textEdit.clear()
        


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()