# Register this blueprint by adding the following line of code 
# to your entry point file.  
# app.register_functions(mcp-tool-function) 
# 
# Please refer to https://aka.ms/azure-functions-python-blueprints


import azure.functions as func
import logging

mcp-tool-function = func.Blueprint()

@mcp-tool-function.mcp_tool()
def mcp_tool_trigger(context: func.MCPToolContext) -> None:
    """
    A simple function that returns a greeting message.
    """
    return "Hello I am MCPTool! Called with context: " + str(context)