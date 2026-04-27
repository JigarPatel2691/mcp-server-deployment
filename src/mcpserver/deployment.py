from fastmcp import FastMCP
import subprocess
import sys

mcp = FastMCP("Demo Jigar")

@mcp.tool()
def add(a: int,b: int) -> int:
    """Add tow numbers"""
    return a+b

@mcp.tool()
def open_application(app_name: str) -> None:
    """Open local application"""
    if not app_name.strip():
        raise ValueError("Application name cannot be empty.")

    try:
        subprocess.run(["open", "-a", app_name], check=True)
        print(f'Successfully opened "{app_name}"')
    except subprocess.CalledProcessError:
        print(f'Could not open application: "{app_name}"')
        sys.exit(1)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 open_mac_app.py <application name>")
        print('Example: python3 open_mac_app.py "Safari"')
        sys.exit(1)

    app_name = " ".join(sys.argv[1:])
    open_application(app_name)