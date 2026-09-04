from openai import OpenAI
import os



endpoint = "https://uzair-anwaar-6-2499-resource.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5-mini"
api_key = "9WfKkdPOmW2WYMxkJSPBtW3ORxT6gI1YoJ5KAWH3zP8B4jzTNBFgJQQJ99CHACHYHv6XJ3w3AAAAACOGspm4"

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

problem = """
A distributed e-commerce system is experiencing intermittent checkout failures 
during peak traffic. The failures appear random, affect roughly 3 percent of the transactions, 
and only occur when inventory checks and payment processing run concurrently. 
Identify the most likely root cause and propose a solution.
"""

response = client.responses.create(
    model=deployment_name,
    instructions="You are a creative copywriter.",
    input=problem,
    temperature=1,
    max_output_tokens=5000,
    reasoning={"effort": "high"}
)

print(f"answer: {response.output[0]}")
