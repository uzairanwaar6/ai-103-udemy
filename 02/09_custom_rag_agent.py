from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import AgentDefinition, PromptAgentDefinition

END_POINT = "https://uzair-anwaar-6-2499-resource.services.ai.azure.com/api/projects/uzair-anwaar-6-2499"
AGENT_NAME = "RagAgent"
DEPLOYMENT = "gpt-5-mini"

SYSTEM_PROMPT = """
You are a customer support assistant for CloudXeus Technology Services.

Answer the customer's question using ONLY the provided sources.

After your answer, cite the source URL you used.

If the sources do not contain the answer, say:
"I don't have that information in the available knowledge base."

Then suggest contacting support@cloudxeus.com.

Never invent policies, prices, refund rules, or timelines.
"""

project_client = AIProjectClient(
    endpoint=END_POINT,
    credential=DefaultAzureCredential()
)

agent_version = project_client.agents.create_version(
    agent_name=AGENT_NAME,
    description="This agent queires data using RAG to answer the questions",
    definition=PromptAgentDefinition(
        model=DEPLOYMENT,
        instructions=SYSTEM_PROMPT
    )
)

print(f"{agent_version.name} is created successfully")
