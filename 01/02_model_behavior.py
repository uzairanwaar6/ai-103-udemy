from openai import OpenAI
import os



endpoint = "https://uzair-anwaar-6-2499-resource.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5-mini"
api_key = "9WfKkdPOmW2WYMxkJSPBtW3ORxT6gI1YoJ5KAWH3zP8B4jzTNBFgJQQJ99CHACHYHv6XJ3w3AAAAACOGspm4"

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

response = client.responses.create(
    model=deployment_name,
    instructions="You are a creative copywriter.",
    input="Write a two-sentence tagline for a new AI-powered productivity app.",
    temperature=1,
    max_output_tokens=5000
)

print(f"answer: {response.output[0]}")
