import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt

form_class = uic.loadUiType("button.ui")[0]

class Window(QMainWindow, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.setText("Push")
        self.pushButton.setEnabled(True)
        self.pushButton.clicked.connect(self.func)

    def func(self) :
        print("Clicked")
        


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()