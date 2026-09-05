from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient


END_POINT = "https://uzair-anwaar-6-2499-resource.services.ai.azure.com/api/projects/uzair-anwaar-6-2499"
AGENT_NAME = "RagAgent"
DEPLOYMENT = "gpt-5-mini"
INDEX_NAME ="aisearch"
SEARCH_ENDPOINT = "https://uzair-resource-foundry-iq-1.search.windows.net"
SEARCH_TEXT = "Can I get my money back?"

client = AIProjectClient(
    endpoint=END_POINT,
    credential=DefaultAzureCredential()
)

agent_client = client.get_openai_client(agent_name= AGENT_NAME)
conversation = agent_client.conversations.create()

search_client = SearchClient(
    endpoint=SEARCH_ENDPOINT,
    credential=DefaultAzureCredential(),
    index_name=INDEX_NAME
    )

search_result = search_client.search(
    search_text=SEARCH_TEXT,
    top=3,
    select=["chunk", "title", "parent_id"],
)

data = ["Title: " + item.get("title","")
        +"\n Parent ID: " + item.get("parent_id","")
        +"\n Chunk: " + item.get("chunk","") 
        for item in search_result]

data = "\n\n\n".join(data)

prompt = f"""
You are a customer support agent for CloudXeus Technology Services.

Answer the customer question using only the sources provided below.
If the sources do not contain enough information, say that the knowledge base does not contain enough information.

Sources:
{data}

Customer question:
{SEARCH_TEXT}
"""

print("\nPrompt sent to agent:\n")


agent_response = agent_client.responses.create(
    input=prompt,
    extra_body={
                "agent_reference": {
                    "name": AGENT_NAME,
                    "type": "agent_reference"
                }
            },
)

print(agent_response.output_text)