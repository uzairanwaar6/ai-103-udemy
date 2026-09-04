from openai import OpenAI
import base64 



endpoint = "https://uzair-anwaar-6-2499-resource.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5-mini"
api_key = "9WfKkdPOmW2WYMxkJSPBtW3ORxT6gI1YoJ5KAWH3zP8B4jzTNBFgJQQJ99CHACHYHv6XJ3w3AAAAACOGspm4"

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)


image_path = "./docs/02. Section Code/Agent_types.png"
with open(image_path, "rb") as image_file:
    file = base64.b64encode(image_file.read()).decode()

input = [
    {
        "role":"user",
        "content":
        [
            {
                "type":"input_text",
                "text": "What are the laws for stealing in Pakistan"
            }
        ]
    }
]
response = client.responses.create(
    model=deployment_name,
    instructions="You are a helpful assistant and you always cite your findings properly.",
    input=input,
    # temperature=0.1,
    max_output_tokens=5000,
    reasoning={"effort": "medium"},
    tool_choice="auto",
    tools=[{"type":"web_search"}]
)

print(f"answer: {response.output_text}")
