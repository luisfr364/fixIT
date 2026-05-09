import os
import time
import subprocess
import asyncio

class SupportScriptsHelper:
    def __init__(self, app):
        self.app = app

    async def run_clean_temp_files_script(self, cb):
        temp_dir = os.environ.get('TEMP', '/tmp')  # Get the temp directory from environment variables



        if not temp_dir or not os.path.exists(temp_dir):
            cb("Diretório temporário não encontrado.")
            return
        
        try:
            # List all files in the temp directory
            files = os.listdir(temp_dir)
            deleted_files_count = 0
            cb(f"Foram encontrados {len(files)} arquivos temporários. Iniciando limpeza...")
            await asyncio.sleep(1)  # Simulate some processing time

            for file in files:
                file_path = os.path.join(temp_dir, file)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)  # Delete the file
                        deleted_files_count += 1
                except Exception as e:
                    cb(f"Erro ao deletar arquivo {file_path}: {e}")

            cb(f"{deleted_files_count} arquivos temporários deletados.")
        except Exception as e:
            cb(f"Erro ao acessar diretório temporário: {e}")
    
    async def run_fix_internet_errors_script(self, cb):   
           await asyncio.sleep(1) # Simulate some processing time
           cb("Iniciando correção de erros de internet...")

           commands = [
             {'command': 'ipconfig /release', 'description': 'Liberando endereço IP...\n'},
             {'command': 'ipconfig /renew', 'description': 'Renovando endereço IP...\n'},
             {'command': 'ipconfig /flushdns', 'description': 'Limpando cache DNS...\n'},
             {'command': 'netsh winsock reset', 'description': 'Resetando Winsock...\n'},
           ]

           for cmd in commands:
               cb(cmd['description'])
               try:
                   await asyncio.sleep(1)
                   result = subprocess.run(cmd['command'], shell=True, capture_output=True, text=True)
                   print(f"Comando: {cmd['command']}\nSaída: {result.stdout}\nErro: {result.stderr}")
                   if result.returncode == 0:
                       cb(f"Comando '{cmd['command']}' executado com sucesso.")
                   else:
                       cb(f"Erro ao executar '{cmd['command']}': {result.stderr}")
               except Exception as e:
                   cb(f"Exceção ao executar '{cmd['command']}': {e}")
    

    async def test_fn(self, cb):
        await asyncio.sleep(1)  # Simulate some async processing time
        cb("Teste de callback funcionando!")


        subprocess.run('echo "Teste de callback funcionando!"', shell=True)




