import slint

class SupportPageController:
    def __init__(self, app):
        self.app = app


    @slint.callback
    def on_script_module_click(self, name, description):
        print(f"Script selecionado: {name} - {description}")
        self.app.selected_script = {"name": name, "description": description}
