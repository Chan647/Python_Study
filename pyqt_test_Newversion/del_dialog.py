from PyQt5 import *
from PyQt5.QtWidgets import *
from db import DB, DB_CONFIG

class Delete(QDialog) :
    def __init__(self) :
        super().__init__()
        self.db = DB(**DB_CONFIG)

        self.setWindowTitle("삭제")
        
        self.did = QLineEdit()

        form = QFormLayout()
        form.addRow("ID", self.did)

        del_btn = QPushButton("삭제")
        del_btn.clicked.connect(self.delete)
        ccl_btn = QPushButton("취소")
        ccl_btn.clicked.connect(self.reject)

        box = QHBoxLayout()
        box.addWidget(del_btn)
        box.addWidget(ccl_btn)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addLayout(box)
        self.setLayout(layout)

    def delete (self) :
        uid = self.did.text().strip()
        uuid = int(uid)

        if not uuid :
            QMessageBox.warning(self, "오류", "ID를 입력하시오")
            self.clear()
            return

        de = self.db.delete_shoes(uuid)

        if de :
            QMessageBox.information(self, "성공", "ID : {}이 삭제되었습니다.".format(uid))
            self.clear()
            self.accept()

        else :
            QMessageBox.critical(self, "실패", "추가 중 오류가 발생하였습니다.")
            self.clear()
            
    
    def clear(self):
            self.did.clear()
        
    
    
    

        