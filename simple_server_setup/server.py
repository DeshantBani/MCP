'''
This is a simple server setup using FastMCP.
It defines a calculator tool that can be called by clients.
'''

from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv("../.env")

mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0",  # only used for SSE transport(localhost)
    port=8050,  #only used for SSE transport(set this to any port)
)


@mcp.tool()  # tool decorator registers the function as a tool
def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    transport = "sse"
    if transport == "stdio":
        print("Running server with stdio transport.")
        mcp.run(transport="stdio")
    elif transport == "sse":
        print("Running server with SSE transport.")
        mcp.run(transport="sse")
    else:
        raise ValueError(f"Unsupported transport: {transport}")

# running the server in development mode: mcp dev server.py
