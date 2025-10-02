from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from db import DB, DB_CONFIG

class Login(QDialog) :
     def __init__(self) :
          super().__init__()
          self.setWindowTitle("로그인")
          self.resize(300,100)
          self.setWindowIcon(QIcon("C:/python_code_Lee/pyqt_test_NewVersion/lock.png"))
          self.db = DB(**DB_CONFIG)

          self.username = QLineEdit()
          self.username.setFixedSize(200,30)
          self.password = QLineEdit()
          self.password.setFixedSize(200,30)
          self.password.setEchoMode(QLineEdit.Password)

          form = QFormLayout()
          form.addRow("아이디",self.username)
          form.addRow("비밀번호",self.password)

          log_btn = QPushButton("로그인")
          log_btn.setFixedHeight(30)
          ap_btn = QPushButton("회원가입")
          ap_btn.setFixedHeight(30)
          log_btn.clicked.connect(self.t_login)
          ap_btn.clicked.connect(self.append_user)

          box = QHBoxLayout()
          box.addWidget(log_btn)
          box.addWidget(ap_btn)

          layout = QVBoxLayout()
          layout.addLayout(form)
          layout.addLayout(box)
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

     def append_user(self) :
          title = QDialog(self)
          title.setWindowTitle("회원 가입")
          self.resize(300,100)

          form =QFormLayout()
          self.append_type = QLineEdit()
          self.append_type.setFixedSize(200,30)
          self.append_inventory = QLineEdit()
          self.append_inventory.setFixedSize(200,30)

          form.addRow("아이디", self.append_type)
          form.addRow("비밀번호", self.append_inventory)

          bac_btn = QPushButton("뒤로 가기")
          bac_btn.setFixedHeight(30)
          bac_btn.clicked.connect(title.reject)
          cpt_btn = QPushButton("완료")
          cpt_btn.setFixedHeight(30)
          cpt_btn.clicked.connect(lambda: self.cpt(title))

          btns = QHBoxLayout()
          btns.addWidget(bac_btn)
          btns.addWidget(cpt_btn)

          root = QVBoxLayout()
          root.addLayout(form)
          root.addLayout(btns)
          title.setLayout(root)

          title.exec_()

     def cpt(self,dialog) :
        id = self.append_type.text().strip()
        pw = self.append_inventory.text().strip()

        if not id or not pw:
          QMessageBox.warning(self, "오류", "아이디와 비밀번호를 모두 입력하세요.")
          return

        ok = self.db.insert_user(id,pw)

        if ok :
          QMessageBox.information(self, "완료", "회원가입이 성공적으로 처리되었습니다.")
          self.append_type.clear()
          self.append_inventory.clear()
          dialog.accept() 




          