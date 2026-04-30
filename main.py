import slint
import time
import shutil
import psutil
import threading
import os
import datetime


import urllib.request

from controllers.welcome_page_controller import WelcomePageController







ui_slint = slint.loader.main_window.MainWindow

class App(ui_slint):
    def __init__(self):
        super().__init__()

        self.welcome_page_controller = WelcomePageController(self)


    

app = App()
app.run()