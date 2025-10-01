from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox
from db_standard import DB, DB_CONFIG

class Login(QDialog) :
     def __init__(self) :
          super().__init__()
          self.setWindowTitle("로그인")
          self.db = DB(**DB_CONFIG)

          self.username = QLineEdit()
          self.username.setFixedSize(200,30)
          self.password = QLineEdit()
          self.password.setFixedSize(200,30)
          self.password.setEchoMode(QLineEdit.Password)

          form = QFormLayout()
          form.addRow("아이디",self.username)
          form.addRow("비밀번호",self.password)

          self.btn_login = QPushButton("로그인")
          self.btn_login.setFixedSize(300,30)
          self.btn_login.clicked.connect(self.t_login)

          layout = QVBoxLayout()
          layout.addLayout(form)
          layout.addWidget(self.btn_login)
          self.setLayout(layout)

     def t_login(self) :
          id = self.username.text().strip()
          pd = self.password.text().strip()

          ok = self.db.verify_user(id,pd)

          if not id or not pd :
               QMessageBox.warning(self, "오류", "아이디와 비밀번호를 모두 입력하세요.")
               return
          
          if ok :
               self.accept()
          else :
               QMessageBox.critical(self, "실패", "아이디 혹은 비밀번호가 올바르지 않습니다.")
          