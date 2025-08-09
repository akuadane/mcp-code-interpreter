# MCP Based Code Interpreter

An MCP server that lets your LLMs execute Python code.


## How to run the server:
 I will try to add this to the list of available servers under `Docker toolkit` very soon. But in the meantime, there are multiple ways to run this server locally.


#### 1. Using Docker MCP Toolkit (Recommended)
'The Docker MCP Toolkit is a gateway that enables seamless setup, management, and execution of containerized MCP servers and their connections to AI agents.' This setup is ideal because it provides a safe environment for the server to execute code without affecting the host computer.

- [Follow this link to setup the server with Docker locally](https://github.com/docker/mcp-registry/blob/main/CONTRIBUTING.md)
- Use this repo when asked to enter a GitHub URL.
- Create a volume that maps to `/app/notebooks` on the container side.

#### 2. Using UV as a package manager
Run the following commands on your terminal and at the root of this repository. 
- `uv pip install .`
- `uv run mcp dev src/server.py` ( to launch the web interface to play with the available tools)
- `uv run mcp install src/server.py` ( to install it to Claude desktop)

## Demo
The following demonstrates one of the use cases. In the video, Claude is using the execute_code tool to write and verify its solution before writing the final solution to the user. It utilizes the session management to access previously executed code.

https://github.com/user-attachments/assets/1ec51325-f27d-4264-84fd-e605a209892e


## Future work
- File upload

#### In case of any security issues, please report them to: akayou.a.kitessa@gmail.com

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/akuadane/mcp-code-interpreter/blob/main/LICENSE) file for details.
