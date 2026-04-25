from fastmcp import FastMCP

mcp = FastMCP("Demo Jigar")

@mcp.tool()
def add(a,b) -> int:
    """Add tow numbers"""
    return a+b