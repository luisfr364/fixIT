import datetime
import platform
import re
import subprocess
import urllib.request

import psutil
import slint


class WelcomePageController:
    def __init__(self, app):
        self.app = app

        # 1. Create the timer instances
        self.timer = slint.Timer()

        self.timer2 = slint.Timer()

        # 2. Start it using the instance method (no self=self needed here)
        # Timer for updating statistics every second
        self.timer.start(
            slint.TimerMode.Repeated,
            datetime.timedelta(seconds=1),
            self.update_statistics,
        )

        # Timer for checking connection every 10 minutes
        self.timer2.start(
            slint.TimerMode.Repeated,
            datetime.timedelta(minutes=10),
            self.check_connection,
        )

        # Executed on startup
        self.check_connection()  # Check connection immediately on startup
        self.get_system_info()

    def update_statistics(self):
        # 1. Coleta os dados (fora do loop da UI para não travar)
        cpu = int(psutil.cpu_percent(interval=None))
        ram = int(psutil.virtual_memory().percent)
        disk = int(psutil.disk_usage("/").percent)

        self.app.cpu_usage = cpu  # Atualiza a propriedade do Slint
        self.app.memory_usage = ram
        self.app.disk_usage = disk

    def check_connection(self):
        try:
            urllib.request.urlopen("http://www.google.com", timeout=5)
            self.app.is_connected = True
            print("Conexão OK")
        except:
            self.app.is_connected = False

    def get_system_info(self):
        cpu_stdout = subprocess.run(
            ["wmic", "cpu", "get", "name"], shell=True, capture_output=True
        ).stdout.decode("utf-8")

        cpu_name = re.findall(
            r"^[^Name][\n]*[\w\W]+[^\W]", cpu_stdout, re.MULTILINE
        )  # Find the cpu name str using regex

        os = platform.platform()

        self.app.system_info = {"os": os, "cpu_name": cpu_name[0].strip()}
