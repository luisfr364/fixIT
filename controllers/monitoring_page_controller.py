import psutil


class MonitoringPageController:
    def __init__(self, app):
        self.app = app

        self.get_detailed_cpu_info()

    def get_detailed_cpu_info(self):

        # Reuse the cpu_name var used to show the name of the cpu in the welcome page
        cpu_name = self.app.system_info["cpu_name"]
        cpu_core_count = psutil.cpu_count(logical=False)
        cpu_thread_count = psutil.cpu_count(logical=True)

        self.app.cpu_info = {
            "cpu_name": cpu_name,
            "cpu_core_count": cpu_core_count,
            "cpu_thread_count": cpu_thread_count,
        }
