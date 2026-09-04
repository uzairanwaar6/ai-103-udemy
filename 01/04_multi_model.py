from openai import OpenAI
import base64 



endpoint = "https://uzair-anwaar-6-2499-resource.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5-mini"
api_key = "9WfKkdPOmW2WYMxkJSPBtW3ORxT6gI1YoJ5KAWH3zP8B4jzTNBFgJQQJ99CHACHYHv6XJ3w3AAAAACOGspm4"

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)


image_path = "../docs/01. Section Code/Agent_types.png"
with open(image_path, "rb") as image_file:
    file = base64.b64encode(image_file.read()).decode()

input = [
    {
        "role":"user",
        "content":
        [
            {
                "type": "input_image",
                "image_url":f"data:image/png;base64,{file}"
            },
            {
                "type":"input_text",
                "text": "Extract the content of this image and present it in tabular format"
            }
        ]
    }
]
response = client.responses.create(
    model=deployment_name,
    instructions="You are a helpful assistant and you extract the information from images.",
    input=input,
    # temperature=0.1,
    max_output_tokens=5000,
    reasoning={"effort": "medium"}
)

print(f"answer: {response.output_text}")
