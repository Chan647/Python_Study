from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, \
QLabel, QLineEdit, QPushButton, QMessageBox, QFormLayout, QDialog
from PyQt5.QtGui import QColor
from db_standard import DB, DB_CONFIG

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("재고 관리")
        self.db = DB(**DB_CONFIG)
    
        self.window = QWidget()
        self.setCentralWidget(self.window)   
        vbox = QVBoxLayout(self.window)

        top_box = QHBoxLayout()
        self.input_type = QLineEdit()
        self.input_type.setFixedHeight(30)
        self.input_showname = QLineEdit()
        self.input_showname.setFixedHeight(30)
        self.input_price = QLineEdit()
        self.input_price.setFixedHeight(30)
        self.input_inventory = QLineEdit()
        self.input_inventory.setFixedHeight(30)
        self.btn_add = QPushButton("추가")
        self.btn_add.setFixedSize(100,30)
        self.btn_add.clicked.connect(self.add)

        top_box.addWidget(QLabel("종류"))
        top_box.addWidget(self.input_type)
        top_box.addWidget(QLabel("상품명"))
        top_box.addWidget(self.input_showname)
        top_box.addWidget(QLabel("가격"))
        top_box.addWidget(self.input_price)
        top_box.addWidget(QLabel("재고"))
        top_box.addWidget(self.input_inventory)
        top_box.addWidget(self.btn_add)

        mid_box = QHBoxLayout()
        self.input_del_type = QLineEdit()
        self.input_del_type.setFixedHeight(30)
        self.delete_btn = QPushButton("제거")
        self.delete_btn.setFixedSize(100,30)
        self.delete_btn.clicked.connect(self.delete) 

        mid_box.addWidget(QLabel("종류"))
        mid_box.addWidget(self.input_del_type)
        mid_box.addWidget(self.delete_btn)

        bot_box = QHBoxLayout()
        self.btn2 = QPushButton("수정")
        self.btn2.setFixedSize(400,40)
        self.btn2.clicked.connect(self.resume_shoes)
        self.btn_suc = QPushButton("완료")
        self.btn_suc.setFixedSize(400,40)
        self.btn_suc.clicked.connect(self.close)

        bot_box.addWidget(self.btn2)
        bot_box.addWidget(self.btn_suc)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["종류","상품명","가격","재고"])
        self.table.setEditTriggers(self.table.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        

        vbox.addLayout(top_box)
        vbox.addLayout(mid_box)
        vbox.addWidget(self.table)
        vbox.addLayout(bot_box)

        self.load_shoes()

    def load_shoes(self) :
        row = self.db.fetch_sup()
        self.table.setRowCount(len(row))
        for r, (type, name, money, num) in enumerate(row) :
            self.table.setItem(r, 0, QTableWidgetItem(type))
            self.table.setItem(r, 1, QTableWidgetItem(name))
            self.table.setItem(r, 2, QTableWidgetItem(str(money)))
            self.table.setItem(r, 3, QTableWidgetItem(str(num)))
        self.table.resizeColumnsToContents()
        self.table.setColumnWidth(0, 80)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 50)

        self.change_color()

    def resume_shoes(self) :
            
        title = QDialog(self)
        title.setWindowTitle("재고 수정")

        form =QFormLayout()
        self.input_rtype = QLineEdit()
        self.input_rtype.setFixedSize(200,40)
        self.input_rinventory = QLineEdit()
        self.input_rinventory.setFixedSize(200,40)

        form.addRow("종류", self.input_rtype)
        form.addRow("재고", self.input_rinventory)

        back_btn = QPushButton("뒤로 가기")
        back_btn.setFixedSize(100, 40)
        back_btn.clicked.connect(title.reject)
        resume_btn = QPushButton("수정")
        resume_btn.setFixedSize(100, 40)
        resume_btn.clicked.connect(self.resume)

        btns = QHBoxLayout()
        btns.addStretch()
        btns.addWidget(back_btn)
        btns.addWidget(resume_btn)

        root = QVBoxLayout()
        root.addLayout(form)
        root.addLayout(btns)
        title.setLayout(root)

        title.exec_()

            
    '''def resume_shoes(self) : 
        r_window = QWidget()
        self.setCentralWidget(r_window)
        r_vbox = QVBoxLayout(r_window)

        box = QVBoxLayout()
        self.input_rtype = QLineEdit()
        self.input_rinventory = QLineEdit()
        
        box.addWidget(QLabel("종류"))
        box.addWidget(self.input_rtype)
        box.addWidget(QLabel("재고"))
        box.addWidget(self.input_rinventory)
       

        u_box = QHBoxLayout()
        self.btn3_add = QPushButton("수정")
        self.btn3_add.clicked.connect(self.resume)
        self.btn4_add = QPushButton("뒤로가기")
        self.btn4_add.clicked.connect(self.back)

        u_box.addWidget(self.btn3_add)
        u_box.addWidget(self.btn4_add)

        r_vbox.addLayout(box)
        r_vbox.addLayout(u_box) '''
    
    def add(self) :
        type = self.input_type.text().strip()
        name = self.input_showname.text().strip()
        money = self.input_price.text().strip()
        num = self.input_inventory.text().strip()

        if not type or not name or not money or not num :
            QMessageBox.warning(self, "오류", "입력창 모두 입력 부탁드립니다")
            self.input_type.clear()
            self.input_showname.clear()
            self.input_price.clear()
            self.input_inventory.clear()
            return
        
        cor = self.db.insert_sup(type,name,money,num)

        if cor :
            QMessageBox.information(self, "완료", "성공적으로 추가되었습니다.")
            self.input_type.clear()
            self.input_showname.clear()
            self.input_price.clear()
            self.input_inventory.clear()
            self.load_shoes()
        else :
            QMessageBox(self, "실패", "추가 중 오류가 발생하였습니다.")


        
    def resume(self) :
        r_type = self.input_rtype.text().strip()
        r_num = self.input_rinventory.text().strip()

        if not r_type or not r_num :
            QMessageBox.warning(self, "오류", "상품명과 개수를 모두 입력하십시오")
            self.input_rtype.clear()
            self.input_rinventory.clear()
            return
        
        rsume = False
        row = self.db.fetch_sup()
        for r,(a,b,c,d) in enumerate(row) :
            if a == r_type :
                rsume = True    
                break
        
        r_cor = self.db.resume_inv(r_num,r_type)

        if not rsume :
            QMessageBox.critical(self, "오류", "상품명이 올바르지 않습니다.\n 다시 확인 부탁드립니다.")
            self.input_rtype.clear()
            self.input_rinventory.clear()
        
        else : 
            if r_cor :
                QMessageBox.information(self, "완료", "성공적으로 수정되었습니다.")
                self.input_rtype.clear()
                self.input_rinventory.clear()
                self.load_shoes()
            else :
                QMessageBox.critical(self, "실패", "오류가 발생하였습니다.")
                self.load_shoes()

    def delete(self) :
        type = self.input_del_type.text().strip()
        
        rsume = False
        row = self.db.fetch_sup()
        for r, (a,b,c,d) in enumerate(row) :
            if a == type :
                rsume = True
                break
            
        delete = self.db.delete_sup(type)

        if not rsume :
            QMessageBox.critical(self, "오류", "입력한 종류의 신발이 없습니다.\n 올바른 종류를 입력하십시오")
            self.input_del_type.clear()
            self.load_shoes()

        else :
            if delete :
                QMessageBox.information(self, "완료", "성공적으로 제거되었습니다.")
                delete
                self.input_del_type.clear()
                self.load_shoes()
                
            else :
                QMessageBox.critical(self, "실패", "오류가 발생하였습니다.")
                self.load_shoes()

    def change_color(self) :
        for row in range(self.table.rowCount()):
            item = self.table.item(row, 3)
            trans = int(item.text())
            if trans >= 5 :
                for col in range(self.table.columnCount()):
                    con = self.table.item(row, col)
                    if con :
                        con.setBackground(QColor("red"))
                    



