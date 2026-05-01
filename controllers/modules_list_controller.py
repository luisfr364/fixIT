import slint

class ModulesListController:
    def __init__(self, app):
        self.app = app

        app.navigate_to = self.on_navigate_to  

    @slint.callback
    def on_navigate_to(self, module_name):
    
        print(f"Navegando para o módulo: {module_name}")
        self.app.current_page = module_name  
        self.app.title = module_name

