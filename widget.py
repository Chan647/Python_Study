from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, \
QLabel, QLineEdit, QPushButton, QMessageBox
from db_standard import DB, DB_CONFIG

class MainWindow(QMainWindow) :
    def __ini__(self) :
        super().__init__()
        self.setWindowTitle("재고 관리")
        self.db = DB(**DB_CONFIG)
    
        window = QWidget()
        self.setCentralWidget(window)   
        vbox = QVBoxLayout(window)

        top_box = QHBoxLayout()
        self.input_type = QLineEdit()
        self.input_showname = QLineEdit()
        self.input_price = QLineEdit()
        self.input_inventory = QLineEdit()
        self.btn_add = QPushButton("추가")
        self.btn_add.clicked.connect(self.add_shoes)

        top_box.addWidget(QLabel("종류"))
        top_box.addWidget(self.input_type)
        top_box.addWidget(QLabel("상품명"))
        top_box.addWidget(self.input_showname)
        top_box.addWidget(QLabel("가격"))
        top_box.addWidget(self.input_price)
        top_box.addWidget(QLabel("재고"))
        top_box.addWidget(self.input_inventory)
        top_box.addWidget(self.btn_add)

        '''bot_box = QHBoxLayout()
        self.btn2_add = QPushButton("수정")
        self.btn2_add.clicked.connect(self.resume_shoes)

        bot_box.addWidget(self.btn2_add)'''

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["종류","상품명","가격","재고"])
        self.table.setEditTriggers(self.table.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)

        vbox.addLayout(top_box)
        vbox.addWidget(self.table)
        #vbox.addWidget(bot_box)

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

    def add_shoes(self) :
        type = self.input_type.text().strip()
        name = self.input_showname.text().strip()
        money = self.input_price.text().strip()
        num = self.input_inventory.text().strip()
        if not type or not name or not money or not num :
            QMessageBox.warning(self, "오류", "입력창 모두 입력 부탁드립니다")

        cor = self.db.insert_sup(type,name,money,num)

        if cor :
            QMessageBox.information(self, "완료", "성공적으로 추가되었습니다.")
            self.input_type.clear()
            self.input_showname.clear()
            self.input_price.clear()
            self.input_inventory.clear()
        else :
            QMessageBox(self, "실패", "추가 중 오류가 발생하였습니다.")
'''
    def resume_shoes(self) : 
        r_window = QWidget()
        self.setCentralWidget(r_window)
        r_vbox = QVBoxLayout(r_window)

        box = QVBoxLayout()
        self.input_rtype = QLineEdit()
        self.input_rinventory = QLineEdit()
        self.btn3_add = QPushButton("수정")
        self.btn3_add.clicked.connect()

        box.addWidget(QLabel("종류"))
        box.addWidget(self.input_rtype)
        box.addWidget(QLabel("재고"))
        box.addWidget(self.input_rinventory)
        box.addWidget(self.btn3_add)

        r_vbox.addLayout(box)

    def resume(self) :
        r_type = self.input_rtype.text().strip()
        r_num = self.input_rinventory.text().strip()

        if not r_type or r_num :
            QMessageBox.warning(self, "오류", "상품명과 개수를 모두 입력하십시오")
            return
        r_cor = self.db.resume_inv(r_num,r_type)

        if r_cor :
            QMessageBox.information(self, "완료", "성공적으로 수정되었습니다.")
            self.input_rtype.clear()
            self.input_rinventory.clear()
            self.load_shoes()
        else :
            QMessageBox.critical(self, "실패", "수정 중 오류가 발생하였습니다.")
        

'''











