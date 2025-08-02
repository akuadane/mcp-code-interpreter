from jupyter_client import KernelManager
from jupyter_client.blocking.client import BlockingKernelClient
from dotenv import load_dotenv
import os
from pathlib import Path


parent_folder  = Path(__file__).resolve().parent
env_path =  parent_folder / '.env'

load_dotenv(dotenv_path=env_path)
notebooks_folder_name = os.getenv('NOTEBOOKS_FOLDER')
notebooks_folder = parent_folder / notebooks_folder_name

class Notebook:
    def __init__(self,session_id):
        self.kernel =  KernelManager()
        self.kernel.start_kernel()
        self.session_id = session_id
        self.client = BlockingKernelClient(connection_file=self.kernel.connection_file)
        self.client.load_connection_file()
        self.client.start_channels()
        self.client.wait_for_ready(timeout=5) 

        self.file_path = os.path.join(notebooks_folder, f'{self.session_id}.txt')

        self.history = []
    
    def execute_new_code(self,code):
        
        result = []
        error = []
        def output_callback(msg):
            if msg['msg_type'] == 'stream':
                result.append(msg['content']['text'])
            elif msg['msg_type'] == 'execute_result':
                result.append(f"Execution Result: {msg['content']['data']['text/plain']}")
            elif msg['msg_type'] == 'error':
                error.append(f"Error: {msg['content']['ename']}: {msg['content']['evalue']}")
        
        
        self.client.execute_interactive(
            code=code,
            output_hook=output_callback,
            stop_on_error=True  # Optional: stop if an error occurs
        )       
        if len(error)==0:
            self.history.append('\n'+code)
        return {"error": error, "result":result}
    
    def dump_to_file(self):
        with open(self.file_path,'w') as f:
            for code in self.history:
                f.write(code+'\n')

    def load_from_file(self):
        try:
            with open(self.file_path) as f:
                code = f.read()
                self.execute_new_code(code)
                return True
        except:
            return False

    # TODO abstract out creating a new client
    def close(self):
        self.kernel.shutdown_kernel()



        

