from PyQt5 import *
from PyQt5.QtWidgets import *
from db import DB, DB_CONFIG

class Resume(QDialog) :
    def __init__(self) :
        super().__init__()
        self.db = DB(**DB_CONFIG)
        self.setWindowTitle("수정")

        self.rid = QLineEdit()
        self.rprice = QLineEdit()
        self.rinven = QLineEdit()
    
        form = QFormLayout()
        form.addRow("ID", self.rid)
        form.addRow("가격", self.rprice)
        form.addRow("재고", self.rinven)

        rsm_btn = QPushButton("수정")
        rsm_btn.clicked.connect(self.resume)
        ccl_btn = QPushButton("취소")
        ccl_btn.clicked.connect(self.reject)
        
        box = QHBoxLayout()
        box.addWidget(rsm_btn)
        box.addWidget(ccl_btn)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addLayout(box)
        self.setLayout(layout)

    def resume(self) :
        uid = self.rid.text().strip()
        price = self.rprice.text().strip()
        inven = self.rinven.text().strip()
        
        if not price and not inven :
            QMessageBox.warning(self, "오류", "가격 또는 재고중 하나를 입력하십시오.")
            self.clear()
            return
        
        if inven == "" and price != "":
            list1 = self.db.update_price_shoes(uid, price)

            if list1 :
                QMessageBox.information(self, "완료", "상품 가격이 수정되었습니다.")
                self.clear()
                self.accept()
            else :
                QMessageBox.critical(self, "실패", "수정 중 오류가 발생하였습니다.")
                self.clear()

        elif inven != "" and price == "":
            list2 = self.db.update_inven_shoes(uid, inven)

            if list2 :
                QMessageBox.information(self, "완료", "상품 재고가 수정되었습니다.")
                self.clear()
                self.accept()
            else :
                QMessageBox.critical(self, "실패", "수정 중 오류가 발생하였습니다.")
                self.clear()

       
        
        

       
        
            
        
        
            
    
    def clear(self):
            self.rid.clear()
            self.rprice.clear()
            self.rinven.clear()
