from PyQt5 import QtTest
from PyQt5.QtWidgets import *
import sys
from GUI import WidgetManager, CustomQt
from GUI.templates import home_template

app = QApplication(sys.argv)


def start():
    window = QMainWindow()
    widget_manager = WidgetManager.WidgetManager(window)

    home_widget = home_template.HomeWidget()
    widget_manager.addWidget(home_widget)

    w = QWidget()
    widget_manager.addWidget(w)
    widget_manager.showWidget(home_widget)





    sys.exit(app.exec_())

start()