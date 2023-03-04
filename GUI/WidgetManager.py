from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class WidgetManager():
    def __init__(self):
        super().__init__()
        self.parent = QMainWindow()

        self.widgets = []


    def addWidget(self, widget: QObject):
        self.widgets.append(widget)

    def setParent(self, widget: QObject):
        if not self.parent.isVisible():
            self.parent.setVisible(True)

        for w in self.widgets:
            if w == widget:
                self.parent.setParent(widget)
                widget.setVisible(True)