from PyQt5.QtWidgets import *
from GUI import CustomQt

class HomeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(10, 10, 1200, 800)
        self.butti = QPushButton(self)
        self.setStyleSheet("background-color: green;")


