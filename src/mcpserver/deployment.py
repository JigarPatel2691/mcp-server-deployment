from fastmcp import FastMCP

mcp = FastMCP("Demo Jigar")

@mcp.tool()
def add(a: int,b: int) -> int:
    """Add tow numbers"""
    return a+b