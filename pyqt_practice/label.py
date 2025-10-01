import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

form_class = uic.loadUiType("label.ui")[0]

class Window(QMainWindow, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lb_control.setText("Hello")
        self.lb_control.setAlignment(Qt.AlignCenter)
        # self.lb_control.setPixmap(QPixmap("as.png"))

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()