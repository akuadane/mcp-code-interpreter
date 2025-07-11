import nbformat as nbf
from nbclient import NotebookClient

class Notebooks:
    def __init__(self):
        self.nb_clients = {}

    
    async def execute_new_code(self,code, session_id):
        if not self.nb_clients.get(session_id):
            nb = nbf.v4.new_notebook()
            client = NotebookClient(nb, kernel_name = "kernel_name='python3'")
            client.nb = nb
            async with client.async_setup_kernel():
                print("setting up the kernel")
                self.nb_clients[session_id] = client

        new_cell = nbf.v4.new_code_cell(code)
        client.nb['cells'].append(new_cell)
        index_of_cell = len(client.nb['cells'])-1
        await client.async_execute_cell(new_cell,index_of_cell )

        results = []
        errors = []
        for output in new_cell.get("outputs", []):
            if output.output_type == "stream":
                results.append(output.text)
            elif output.output_type == "execute_result":
                results.append(output.data.get("text/plain", ""))
            elif output.output_type == "error":
                errors.append("Error:", output.evalue)        
        
        return {"errors": errors, "results":results}
    
    def dump_to_file(self):
        for session_id, client in self.nb_clients.items():
            with open('f{session_id}.ipynb') as f:
                nbf.write(client.nb,f)

    # TODO load from file

    # TODO abstract out creating a new client
    



        

