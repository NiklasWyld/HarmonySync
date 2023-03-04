import Backend, Assets, GUI, savedata
from GUI import main
from infi.systray import SysTrayIcon

def launchUI(systray):
    main.start()

def check(systray):
    pass

menu_options = (('Open HarmonySync', None, launchUI), ("Check", None, check))
systray_icon = SysTrayIcon(None, 'HarmonySync', menu_options)


def start():
    systray_icon.start()

def shutdown():
    systray_icon.shutdown()

systray_icon.start()