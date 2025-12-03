from fastmcp import FastMCP

mcp = FastMCP("Custom Server")

@mcp.tool
def basi_tool():
    """return a string that has no inherent meaning."""
    return "This is a tool for just show case."