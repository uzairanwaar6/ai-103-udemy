from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent

endpoint="https://uzair-anwaar-6-2499-resource.openai.azure.com/openai/v1"
deployment_name="gpt-5-mini"
api_key="9WfKkdPOmW2WYMxkJSPBtW3ORxT6gI1YoJ5KAWH3zP8B4jzTNBFgJQQJ99CHACHYHv6XJ3w3AAAAACOGspm4"


model=ChatOpenAI(
    base_url=endpoint,
    api_key=api_key,
    model=deployment_name
)

@tool
def get_order_status(order_id: str) -> str:
    """Get the current status of a CloudXeus order by order ID."""
    orders = {
        "ORD-001": "Dispatched — arriving tomorrow.",
        "ORD-002": "Processing — not yet shipped.",
        "ORD-003": "Delivered on June 12, 2026.",
    }
    return orders.get(order_id, f"Order {order_id} not found.")

@tool
def get_inventory(product_id: str) -> str:
    """Check the available inventory for a CloudXeus product by product ID."""
    inventory = {
        "PRD-A1": "142 units in stock.",
        "PRD-B2": "0 units — out of stock.",
        "PRD-C3": "37 units in stock.",
    }
    return inventory.get(product_id, f"Product {product_id} not found.")

agent = create_agent(
    name="LangChainAgent",
    model=model,
    tools=[get_order_status, get_inventory],
    system_prompt="You are a helpful operations assistant. Use the available tools to answer questions accurately.",
)

response = agent.invoke(
    {
        "messages":[
            {
                "role":"user",
                "content":"Give me inventory status of PRD-B2 and status of the order number ORD-003"
            }]
    }
)

print(response["messages"][-1].content)