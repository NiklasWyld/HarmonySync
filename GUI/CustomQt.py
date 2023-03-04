import PyQt5
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.widget = QWidget()
        self.widget.setStyleSheet("border-radius: 40px; background-color: white")
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)


class QMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()


    def setupUI(self):
        self.setMinimumSize(300, 150)
        self.setWindowFlag(Qt.FramelessWindowHint)
