import sys
from login import Login
from PyQt5.QtWidgets import QApplication
from widget import MainWindow

if __name__ == "__main__" :

    app = QApplication(sys.argv)

    login = Login()
    
    if login.exec_() == Login.Accepted :
        w = MainWindow()
        w.show()
        sys.exit(app.exec_())
    else :
        sys.exit(0)