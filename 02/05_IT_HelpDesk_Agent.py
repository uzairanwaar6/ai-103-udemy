from azure.ai.projects import AIProjectClient
from azure.identity  import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition, WebSearchTool, FunctionTool

END_POINT = "https://uzair-anwaar-6-2499-resource.services.ai.azure.com/api/projects/uzair-anwaar-6-2499"
AGENT_NAME = "ITHelpDeskAgent"
DEPLOYMENT = "gpt-5-mini"

client = AIProjectClient(
    endpoint=END_POINT,
    credential=DefaultAzureCredential()
)

tools = [
    WebSearchTool(),
    FunctionTool(
        name="get_password_reset_steps",
        description="Get the company password reset steps.",
        strict=True,
        parameters={
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        }
    ),
    FunctionTool(
            name="get_vpn_troubleshooting_steps",
            description="Get troubleshooting steps for VPN connection issues.",
            parameters={
                "type": "object",
                "properties": {},
                "required": [],
                "additionalProperties": False,
            },
            strict=True,
        ),
        FunctionTool(
            name="get_software_install_guide",
            description="Get installation instructions for a supported software package.",
            parameters={
                "type": "object",
                "properties": {
                    "software_name": {
                        "type": "string",
                        "description": "The software name, for example Slack, Zoom, or VS Code."
                    }
                },
                "required": ["software_name"],
                "additionalProperties": False,
            },
            strict=True
        )
       
]

agent  = client.agents.create_version(
    agent_name=AGENT_NAME,
    description="This agent provides help according to company defined policy",
    definition=PromptAgentDefinition(
        instructions=     "You are an IT support assistant for a company. "
                    "Help users with password resets, VPN issues, and software installation. "
                    "Give clear, step-by-step answers. "
                    "If the question is outside IT support topics, politely say so.",
        model=DEPLOYMENT,
        tools=tools
    )
)

print(f"Agent created:")
print(f"  ID      : {agent.id}")
print(f"  Name    : {agent.name}")
print(f"  Version : {agent.version}")

# client.agents.delete(agent.name,force=True)

# print("Agent Deleted")