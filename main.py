import slint
import time
import shutil
import psutil
import threading
import os
import datetime


import urllib.request







ui_slint = slint.loader.WelcomeWindow.welcome_window.WelcomeWindow

class App(ui_slint):
    def __init__(self):
        super().__init__()
        self.cpu_usage = 5

        # 1. Create the timer instances
        self.timer = slint.Timer()

        self.timer2 = slint.Timer()

        # 2. Start it using the instance method (no self=self needed here)
        # Timer for updating statistics every second
        self.timer.start(
            slint.TimerMode.Repeated, 
            datetime.timedelta(seconds=1), 
            self.update_statistics
            )
        
        # Timer for checking connection every 10 minutes
        self.timer2.start(
            slint.TimerMode.Repeated, 
            datetime.timedelta(minutes=10), 
            self.check_connection
            )
        
        self.check_connection()  # Check connection immediately on startup
        


    def update_statistics(self):
        # 1. Coleta os dados (fora do loop da UI para não travar)
        cpu = int(psutil.cpu_percent(interval=None))
        ram = int(psutil.virtual_memory().percent)
        disk = int(psutil.disk_usage('/').percent)

        self.cpu_usage = cpu
        self.memory_usage = ram
        self.disk_usage = disk

    def check_connection(self):
        try:
            urllib.request.urlopen('http://www.google.com', timeout=5)
            self.is_connected = True
            print("Conexão OK")
        except:
            self.is_connected = False

app = App()
app.run()