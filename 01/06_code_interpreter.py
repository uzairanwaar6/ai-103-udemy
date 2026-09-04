from openai import OpenAI
import base64 



endpoint = "https://uzair-anwaar-6-2499-resource.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5-mini"
api_key = "9WfKkdPOmW2WYMxkJSPBtW3ORxT6gI1YoJ5KAWH3zP8B4jzTNBFgJQQJ99CHACHYHv6XJ3w3AAAAACOGspm4"

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)


input = [
    {
        "role":"user",
        "content":
        [
            {
                "type":"input_text",
                "text": "What is the compound interest on $10,000 at 5 percent annual rate over 10 years?"
            }
        ]
    }
]
response = client.responses.create(
    model=deployment_name,
    instructions="You are a data analyst. Use Python to calculate precisely.",
    input=input,
    # temperature=0.1,
    max_output_tokens=5000,
    reasoning={"effort": "medium"},
    tool_choice="auto",
    tools=[
            {"type":"web_search"}, 
            {"type":"code_interpreter", "container": {"type": "auto", "memory_limit":"1g"}}]
)

# Inspect what happened under the hood
for item in response.output:
    if item.type == "code_interpreter_call":
        print("=== Python Code the Model Wrote ===")
        print(item.code)
        print("\n=== Output from Execution ===")
        print(item.outputs)
    elif item.type == "message":
        print("\n=== Final Answer ===")
        print(response.output_text)
