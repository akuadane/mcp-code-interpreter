# MCP Based Code Interpreter

An MCP server that lets your LLMs execute python code.


## How to run the server:
 I will try to add this to the list of available servers under `Docker toolkit` very soon. But in the meantime, there are multiple ways to run this server locally.


#### 1. Using Docker MCP Toolkit (Recommended)
'The Docker MCP Toolkit is a gateway that enables seamless setup, management, and execution of containerized MCP servers and their connections to AI agents.' This setup is ideal because it provides a safe environment for the server to execute code without affecting the host computer.

- [Follow this link to setup the server with docker locally](https://github.com/docker/mcp-registry/blob/main/CONTRIBUTING.md)
- Use this repo when asked to enter a Github URL.

#### 2. Using UV as a package manager
Run the following commands on your terminal and at the root of this repository. 
- `uv pip install .`
- `uv run mcp dev src/server.py` ( to launch the web interface to play with the available tools)
- `uv run mcp install src/server.py` ( to install it to Claude desktop)
