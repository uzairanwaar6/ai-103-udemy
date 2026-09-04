from azure.ai.projects import AIProjectClient
from azure.identity  import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition, AgentDefinition
import json
from helpdesk_functions import run_local_function

END_POINT = "https://uzair-anwaar-6-2499-resource.services.ai.azure.com/api/projects/uzair-anwaar-6-2499"
AGENT_NAME = "ITHelpDeskAgent"
AGENT_VERSION = "1"

client = AIProjectClient(
    endpoint=END_POINT,
    credential=DefaultAzureCredential()
)

openai_client = client.get_openai_client()
conversation = openai_client.conversations.create()


response = openai_client.responses.create(
  conversation=conversation.id,
  input="How to reset my company pc password?",
  extra_body=
    {
        "agent_reference":
        {
            "name":AGENT_NAME, 
            "type":"agent_reference",
            "version": AGENT_VERSION,
        }
    }   
)

tool_outputs=[]

for item in response.output:
    if item.type == "function_call":
        function_name = item.name
        arguments = json.loads(item.arguments)

        print(f"Function requested: {function_name}")
        print(f"Arguments received: {arguments}")

        function_result = run_local_function(function_name, arguments)

        tool_outputs.append(
            {
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": function_result,
            }
        )

if tool_outputs:
    final_response = openai_client.responses.create(
        conversation=conversation.id,
        input=tool_outputs,
        extra_body={
            "agent_reference": {
                "type": "agent_reference",
                "name": AGENT_NAME,
                "version": AGENT_VERSION,
            }
        },
    )

    print(final_response.output_text)

else:
    print(response.output_text)