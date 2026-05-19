import slint

from helpers.support_scripts_helper import SupportScriptsHelper


class SupportPageController:
    def __init__(self, app):
        self.app = app

    # Add a new line to the console output in the UI
    # Used on the callback of the script execution to show the output of the script in the console
    @slint.callback
    def update_console_output(self, new_message):
        message = self.app.console_output
        self.app.console_output = message + "\n" + new_message

    @slint.callback
    def on_script_module_click(self, name, description):
        print(f"Script selecionado: {name} - {description}")
        self.app.selected_script = {
            "name": name,
            "description": description,
            "name_short": name[:24] + "..." if len(name) > 24 else name,
        }  # Example: truncate name to first 24 characters

    # Call the scripts helper to run the scripts based on the selected_script var
    @slint.callback
    async def on_run_script(self):
        helper = SupportScriptsHelper(self.app)
        selected_script = (
            self.app.selected_script
        )  # Gets the selected_script var value from the main window

        match (
            selected_script.name
        ):  # Decide which script to run based on the selected script
            case "Limpeza de Arquivos Temporários":
                await helper.run_clean_temp_files_script(self.update_console_output)
            case "Correção de erros de internet":
                await helper.run_fix_internet_errors_script(self.update_console_output)
            case "Test":
                await helper.test_fn(self.update_console_output)
            case _:
                self.update_console_output("Script ainda não implementado.")
