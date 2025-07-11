import nbformat as nbf
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

import asyncio



async def execute_cell():
            
    nb = nbf.v4.new_notebook()
    cell1 = nbf.v4.new_code_cell('result = 10**2')
    cell2 = nbf.v4.new_code_cell("print('result=',result)")
    
    nb['cells'] = [cell1, cell2]
    with open('test.ipynb','w') as f:
        nbf.write(nb,f)

    # Load the notebook
    with open("test.ipynb") as f:
        nb = nbf.read(f, as_version=4)

    # Create the execution client
    client = NotebookClient(nb)
    nb['cells'].append(nbf.v4.new_code_cell("1000*2 + 421, 100"))
    client.nb = nb
    print(client.nb)
    # Run cell-by-cell manually
    # for i, cell in enumerate(nb.cells):
    #     if cell.cell_type != "code":
    #         continue
    #     try:
    #         print(cell)
    #         client.execute_cell(cell, i)
    #         print(f"Executed cell {i}: OK")
    #     except CellExecutionError as e:
    #         print(f"Error in cell {i}: {e}")
    #         break  # or continue, depending on your use case

    # client.execute()
    async with client.async_setup_kernel():
        for i, cell in enumerate(nb.cells):
            if cell.cell_type == "code":
                print(f"{cell['source']}")
                print(f"\nOutputs from cell {i}:")
                await client.async_execute_cell(cell,i)
                print('outputs',cell.get("outputs", []))
                for output in cell.get("outputs", []):
                    if output.output_type == "stream":
                        print(output.text)
                    elif output.output_type == "execute_result":
                        print(output.data.get("text/plain", ""))
                    elif output.output_type == "error":
                        print("Error:", output.evalue)

    # Save notebook with outputs
    with open("executed_notebook.ipynb", "w") as f:
        nbf.write(nb, f)


if __name__ == '__main__':
    asyncio.run(execute_cell())