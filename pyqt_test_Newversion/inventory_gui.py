from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from db import DB, DB_CONFIG
from resume_dialog import Resume
from add_dialog import Add
from del_dialog import Delete

class mainWindow(QMainWindow) : 
    def __init__(self) :
        super().__init__()
        self.db = DB(**DB_CONFIG)
        
        self.setWindowTitle("신발 창고")
        self.resize(600,300)
        self.setWindowIcon(QIcon("C:/python_code_Lee/pyqt_test_NewVersion/shoe.png"))
        
        central = QWidget()
        self.setCentralWidget(central)
        box = QVBoxLayout(central)

        btn_box = QHBoxLayout()
        rsm_btn = QPushButton("수정")
        add_btn = QPushButton("추가")
        del_btn = QPushButton("제거")
        suc_btn = QPushButton("완료")

        rsm_btn.clicked.connect(self.resume_dialog)
        rsm_btn.setFixedHeight(30)
        add_btn.clicked.connect(self.add_dialog)
        add_btn.setFixedHeight(30)
        del_btn.clicked.connect(self.del_dialog)
        del_btn.setFixedHeight(30)
        suc_btn.clicked.connect(self.close)
        suc_btn.setFixedHeight(30)

        btn_box.addWidget(rsm_btn)
        btn_box.addWidget(add_btn)
        btn_box.addWidget(del_btn)
        btn_box.addWidget(suc_btn)
        

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID","종류","상품명","가격","재고"])
        self.table.setEditTriggers(self.table.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)

        box.addWidget(self.table)
        box.addLayout(btn_box)

        self.load_shoes()

    def load_shoes(self) :
        rows = self.db.fetch_shoes()
        self.table.setRowCount(len(rows))

        for r, (ID, type, name, price, inventory) in enumerate(rows) :
            self.table.setItem(r, 0, QTableWidgetItem(str(ID)))
            self.table.setItem(r, 1, QTableWidgetItem(type))
            self.table.setItem(r, 2, QTableWidgetItem(name))
            self.table.setItem(r, 3, QTableWidgetItem(price))
            self.table.setItem(r, 4, QTableWidgetItem(str(inventory)))
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.change_color()

    def resume_dialog(self) :
        dialog = Resume()
        if dialog.exec() == Resume.Accepted :
            self.load_shoes()

    def add_dialog(self) :
        dialog = Add() 
        if dialog.exec_() == Add.Accepted :
            self.load_shoes()

    def del_dialog(self) :
        dialog = Delete()
        if dialog.exec_() == Delete.Accepted :
            self.load_shoes()

    def change_color(self) :
        for row in range(self.table.rowCount()):
            item = self.table.item(row, 4)
            trans = int(item.text())
            if trans >= 5 :
                for col in range(self.table.columnCount()):
                    con = self.table.item(row, col)
                    if con :
                        font = QFont()
                        font.setWeight(99)
                        font.setPointSize(12)
                        con.setBackground(QColor("red"))
                        con.setFont(font)
        