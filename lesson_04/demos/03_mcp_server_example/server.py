"""Minimalny serwer MCP -- wystawia narzedzie do czytania plikow przez Model Context Protocol."""

import os
import json
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

server = Server("file-reader")


@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="read_file",
            description="Read the contents of a text file from disk",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Absolute or relative path to the file",
                    },
                },
                "required": ["path"],
            },
        ),
        Tool(
            name="list_directory",
            description="List files and folders in a directory",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the directory",
                    },
                },
                "required": ["path"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "read_file":
        path = arguments["path"]
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            if len(content) > 5000:
                content = content[:5000] + "\n\n... (uciete na 5000 znakow)"
            return [TextContent(type="text", text=content)]
        except FileNotFoundError:
            return [TextContent(type="text", text=f"Plik nie znaleziony: {path}")]
        except Exception as e:
            return [TextContent(type="text", text=f"Blad: {e}")]

    elif name == "list_directory":
        path = arguments["path"]
        try:
            entries = os.listdir(path)
            result = "\n".join(
                f"[DIR] {e}" if os.path.isdir(os.path.join(path, e)) else f"[FILE] {e}"
                for e in sorted(entries)
            )
            return [TextContent(type="text", text=result)]
        except Exception as e:
            return [TextContent(type="text", text=f"Blad: {e}")]

    return [TextContent(type="text", text=f"Nieznane narzedzie: {name}")]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
