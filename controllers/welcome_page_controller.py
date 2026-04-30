import datetime
import psutil
import urllib.request
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

        self.app.cpu_usage = cpu  # Atualiza a propriedade do Slint
        self.app.memory_usage = ram
        self.app.disk_usage = disk

    def check_connection(self):
        try:
            urllib.request.urlopen('http://www.google.com', timeout=5)
            self.app.is_connected = True
            print("Conexão OK")
        except:
            self.app.is_connected = False
