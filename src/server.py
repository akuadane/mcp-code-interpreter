import time
from mcp.server.fastmcp import FastMCP, Context
from notebook import Notebook

mcp = FastMCP(name = 'Code Interpreter", "2.0.0", "A simple code interpreter that executes Python code and returns the result.',
              instructions= """
                You can execute Python code by sending a request with the code you want to run.
                Make sure to include the `result` variable in your code to return the output.
                For example:
                ```python
                x = 10
                y = 20
                result = x + y
                ```
                )""")
notebook = None

@mcp.tool('execute_code: 2.0.0')
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
    if session_id==0 or (notebook and notebook.session_id!=session_id):
        session_id = int(time.time())
        notebook = Notebook(session_id)
        await ctx.info(f"Your session_id for this chat is {session_id}. You should provide it for subsequent requests.")

    try:
        return notebook.execute_new_code(code)
    except Exception as e:
        return {'error':str(e), 'result':[] }


if __name__ == '__main__':
    mcp.run()