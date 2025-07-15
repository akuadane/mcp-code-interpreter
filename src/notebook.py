from jupyter_client import KernelManager
from jupyter_client.blocking.client import BlockingKernelClient

class Notebook:
    def __init__(self, session_id):
        self.kernel =  KernelManager()
        self.kernel.start_kernel()
        
        self.client = BlockingKernelClient(connection_file=self.kernel.connection_file)
        self.client.load_connection_file()
        self.client.start_channels()
        self.client.wait_for_ready(timeout=5) 

        self.session_id = session_id

        self.history = []
    
    def execute_new_code(self,code):
        self.history.append(code)
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
       
        return {"error": error, "result":result}
    
    def dump_to_file(self):
        with open(f'{self.session_id}.txt','w') as f:
            for code in self.history:
                f.write(code+'\n')

    def load_from_file(self):
        try:
            with open(f'{self.session_id}.txt') as f:
                code = f.read()
                self.execute_new_code(code)
        except:
            print("Can't open file.")

    # TODO abstract out creating a new client
    def close(self):
        self.kernel.shutdown_kernel()



        

