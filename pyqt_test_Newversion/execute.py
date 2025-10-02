from inventory_gui import mainWindow
from PyQt5.QtWidgets import QApplication
from login import Login
import sys

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    
    login = Login()
    
    if login.exec_() == Login.Accepted :
        w = mainWindow()
        w.show()
        sys.exit(app.exec_())
    else :
        sys.exit(0)
