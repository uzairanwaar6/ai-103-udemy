# pip install langchain langchain-openai
from langchain_openai import ChatOpenAI

endpoint="https://uzair-anwaar-6-2499-resource.openai.azure.com/openai/v1"
deployment_name="gpt-5-mini"
api_key="9WfKkdPOmW2WYMxkJSPBtW3ORxT6gI1YoJ5KAWH3zP8B4jzTNBFgJQQJ99CHACHYHv6XJ3w3AAAAACOGspm4"


client=ChatOpenAI(
    base_url=endpoint,
    api_key=api_key,
    model=deployment_name
)

response=client.invoke("What are the three main benefits of using managed AI endpoints in the cloud?")
print(response.content)