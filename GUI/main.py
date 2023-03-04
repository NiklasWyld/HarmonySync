from PyQt5 import QtTest
from PyQt5.QtWidgets import *
import sys
from GUI import WidgetManager, CustomQt
from GUI.templates import home_template

app = QApplication(sys.argv)


def start():
    window = QMainWindow()
    widget_manager = WidgetManager.WidgetManager()

    home_widget = home_template.HomeWidget()
    widget_manager.addWidget(home_widget)
    widget_manager.setParent(home_widget)

    sys.exit(app.exec_())

start()