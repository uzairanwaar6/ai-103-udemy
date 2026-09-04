from azure.ai.projects import AIProjectClient
from azure.identity  import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition, WebSearchTool

END_POINT = "https://uzair-anwaar-6-2499-resource.services.ai.azure.com/api/projects/uzair-anwaar-6-2499"
AGENT_NAME = "WebSearchAgent"
DEPLOYMENT = "gpt-5-mini"

client = AIProjectClient(
    endpoint=END_POINT,
    credential=DefaultAzureCredential()
)

agent  = client.agents.create_version(
    agent_name=AGENT_NAME,
    description="This agent provides help according to company defined policy",
    definition=PromptAgentDefinition(
        instructions=  "You are a helpful assistant. Use web search to answer questions that require current information.",
        model=DEPLOYMENT,
        tools=[WebSearchTool()]
    )
)

print(f"Agent created:")
print(f"  ID      : {agent.id}")
print(f"  Name    : {agent.name}")
print(f"  Version : {agent.version}")

# client.agents.delete(agent.name,force=True)

# print("Agent Deleted")