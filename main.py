from fastmcp import FastMCP
import random
import json

# create MCP server instance
mcp = FastMCP("Simple calculator Server")

@mcp.tool
def add(a : float , b : float)->float:
    """Add two numbers together.
    
    Args:
        a : First number
        b : Second number
        
    Returns:
        Sum of two number"""
    return a+b

@mcp.tool
def random_number(min_val : int=1 , max_val : int = 100)->int:
    """Generate a random number within range 

    Args:
        min_val : Minimum Value
        max_val : Maximum Value

    Returns:
        A random number b/w min_val and max_val 

    """
    return random.randint(min_val,max_val)

@mcp.resource('info://server')
def server()->str:
    """Get information about server"""
    info = {
        'name' : 'Simple calculator server',
        'version' : '1.0.0',
        'discription' : 'A basic MCP server with math tool',
        'tools' : '[add,random_number] '
    }
    return json.dumps(info,indent=2)



if __name__ == "__main__":
    mcp.run(transport="http",host = '0.0.0.0',port = 8000)