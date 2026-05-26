import slint

from controllers.modules_list_controller import ModulesListController
from controllers.support_page_controller import SupportPageController
from controllers.welcome_page_controller import WelcomePageController

# Loads the main window from the .slint file and creates a class for it
ui_slint = slint.loader.main_window.MainWindow


class App(ui_slint):
    def __init__(self):
        super().__init__()

        # Connect the controllers to the main window
        self.welcome_page_controller = WelcomePageController(self)
        self.modules_list_controller = ModulesListController(self)
        self.support_page_controller = SupportPageController(self)

        # Connect the functions defined in the controllers to the callbacks defined
        # in main_window.slint
        self.handle_script_module_select = (
            self.support_page_controller.on_script_module_click
        )

        self.navigate_to = self.modules_list_controller.on_navigate_to
        self.handle_script_execution = self.support_page_controller.on_run_script


app = App()
app.run()
