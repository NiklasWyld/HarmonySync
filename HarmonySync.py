from PyQt5 import QtTest
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import json
import os
from gui import CustomQt
from backend import *
import threading
import multiprocessing
from gui.templates import home_template, settings_template

app_version = "Alpha"
app_path = os.getcwd()

save_data = json.loads(open(f"{app_path}/save_data.json", "r").read())

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

window = QMainWindow()

home_widget = home_template.HomeWidget(window)
settings_widget = settings_template.SettingsWidget(window)

def startGUI():
    home_widget.show()




systray_icon = QSystemTrayIcon()
systray_icon.setIcon(QIcon(f"{app_path}/assets/logo.png"))
systray_icon.setVisible(True)

systray_menu = QMenu()

startGUI_action = QAction("Open HarmonySync")

quit_action = QAction("Quit")
quit_action.triggered.connect(app.quit)

systray_menu.addActions([startGUI_action, quit_action])

systray_icon.setContextMenu(systray_menu)

if __name__ == "__main__":
    startGUI()
    sys.exit(app.exec_())
