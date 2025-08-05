'''
Connecting to the MCP server using SSE (Server-Sent Events) transport.
This client connects to the calculator server running on port 8050.
'''

import asyncio
import httpx
from mcp import ClientSession
from mcp.client.sse import sse_client


async def main(): 
    # Connect to the SSE server
    async with sse_client("http://localhost:8050/sse") as (read_stream,
                                                           write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tools_result = await session.list_tools()
            print("Available tools:")
            for tool in tools_result.tools:
                print(f"  - {tool.name}: {tool.description}")

            # Call our calculator tool
            result = await session.call_tool("add", arguments={"a": 2, "b": 3})
            print(f"2 + 3 = {result.content[0].text}")

            # Test with different numbers
            result2 = await session.call_tool("add",
                                              arguments={
                                                  "a": 10,
                                                  "b": 25
                                              })
            print(f"10 + 25 = {result2.content[0].text}")


if __name__ == "__main__":
    asyncio.run(main())
