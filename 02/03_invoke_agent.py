from azure.ai.projects import AIProjectClient
from azure.identity  import DefaultAzureCredential

END_POINT = "https://uzair-anwaar-6-2499-resource.services.ai.azure.com/api/projects/uzair-anwaar-6-2499"
AGENT_NAME = "HelpDeskAgent"
DEPLOYMENT = "gpt-5-mini"

client = AIProjectClient(
    endpoint=END_POINT,
    credential=DefaultAzureCredential()
)

openai_client = client.get_openai_client()

response = openai_client.responses.create(
  input="How to reset my company pc password?",
  extra_body={"agent_reference":{"name":AGENT_NAME, "type":"agent_reference"}}   
)

print(response.output_text)