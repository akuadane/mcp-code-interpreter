import time
from mcp.server.fastmcp import FastMCP, Context
from notebook import Notebook


mcp = FastMCP(name = 'Code Interpreter", "2.0.0", "A simple code interpreter that executes Python code and returns the result.',
              instructions= """
                You can execute Python code by sending a request with the code you want to run.
                Think of this tool as a jupyter notebook. It will remember your previously executed code, if you pass in your session_id. 
                It is crucial to remember your session_id for a smooth interaction.
                ```
                )""")
notebook = None

@mcp.tool('execute_code')
async def execute_code(code: str,ctx: Context, session_id: int = 0) -> dict:
    global notebook
    """
    Executes the provided Python code and returns the result.
    
    Args:
        code (str): The Python code to execute.
        session_id (int, optional): A unique identifier used to associate multiple code execution requests
            with the same logical session. If this is the first request, you may omit it or set it to 0.
            The system will generate and return a new session_id, which should be reused in follow-up requests
            to maintain continuity within the same session.
    
    Returns:
        dict: A dictionary containing the result or an error message.
    """
    session_info = None
    if session_id==0 or (notebook and notebook.session_id!=session_id):
        session_id = int(time.time())
        notebook = Notebook(session_id)
        session_info = f"Your session_id for this chat is {session_id}. You should provide it for subsequent requests."

    try:
        result = notebook.execute_new_code(code)
        if session_info:
            result['result'].append(session_info)
        
        return result 
    except Exception as e:
        return {'error':str(e), 'result':[] }



if __name__ == '__main__':
    mcp.run()