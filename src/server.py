from mcp.server.fastmcp import FastMCP, Context


mcp = FastMCP(name = 'Code Interpreter", "1.0.0", "A simple code interpreter that executes Python code and returns the result.',
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


@mcp.tool('execute_code')
def execute_code(code: str, ctx: Context) -> dict:
    """
    Executes the provided Python code and returns the result.
    
    Args:
        code (str): The Python code to execute.
    
    Returns:
        dict: A dictionary containing the result or an error message.
    """
    with open('context.txt','w') as f:
        f.write(str(ctx))
    output = {
        'error': None,
        'result': None,
    }
    try:
        loc = {}
        exec(code, globals(), loc)
        result = loc.get('result', 'No result found. Make sure to assign the output to the `result` variable.')
        output['result'] = result
    except Exception as e:
        output['error'] = str(e)
    finally:
        return output


if __name__ == '__main__':
    mcp.run()