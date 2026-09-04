from azure.ai.projects import AIProjectClient
from azure.identity  import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition, AgentDefinition

END_POINT = "https://uzair-anwaar-6-2499-resource.services.ai.azure.com/api/projects/uzair-anwaar-6-2499"
AGENT_NAME = "HelpDeskAgent"
DEPLOYMENT = "gpt-5-mini"

client = AIProjectClient(
    endpoint=END_POINT,
    credential=DefaultAzureCredential()
)

agent  = client.agents.create_version(
    agent_name=AGENT_NAME,
    description="This agent provides help according to company defined policy",
    definition=PromptAgentDefinition(
        instructions= "You are an IT support assistant for a company. "
                    "Help users with password resets, VPN issues, and software installation. "
                    "Give clear, step-by-step answers. "
                    "If the question is outside IT support topics, politely say so.",
        model=DEPLOYMENT
    )
)

print(f"Agent created:")
print(f"  ID      : {agent.id}")
print(f"  Name    : {agent.name}")
print(f"  Version : {agent.version}")

# client.agents.delete(agent.name,force=True)

# print("Agent Deleted")