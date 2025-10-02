from PyQt5 import *
from PyQt5.QtWidgets import *
from db import DB, DB_CONFIG

class Add(QDialog) :
    def __init__(self) :
        super().__init__()
        self.db = DB(**DB_CONFIG)

        self.setWindowTitle("추가")
        
        self.atype = QLineEdit()
        self.aname = QLineEdit()
        self.aprice = QLineEdit()
        self.ainven = QLineEdit()
       
        form = QFormLayout()
        form.addRow("종류", self.atype)
        form.addRow("상품명", self.aname)
        form.addRow("가격", self.aprice)
        form.addRow("재고", self.ainven)

        add_btn = QPushButton("추가")
        add_btn.clicked.connect(self.add)
        ccl_btn = QPushButton("취소")
        ccl_btn.clicked.connect(self.reject)

        box = QHBoxLayout()
        box.addWidget(add_btn)
        box.addWidget(ccl_btn)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addLayout(box)
        self.setLayout(layout)

    def add(self) : 
        type = self.atype.text().strip()
        name = self.aname.text().strip()
        price = self.aprice.text().strip()
        inven = self.ainven.text().strip()

        if not type or not name or not price or not inven :
            QMessageBox.warning(self, "오류", "모든 항목을 입력하십시오.")
            self.clear()
            return

        list = self.db.insert_shoes(type,name,price,inven)

        if list :
            QMessageBox.information(self, "완료", "상품이 추가되었습니다.")
            self.clear()
            self.accept()
        else :
            QMessageBox.critical(self, "실패", "추가 중 오류가 발생하였습니다.")
            self.clear()
            
    
    def clear(self):
            self.atype.clear()
            self.aname.clear()
            self.aprice.clear()
            self.ainven.clear()

        
        

        
        