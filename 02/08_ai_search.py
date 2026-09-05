from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient


search_client = SearchClient(
    endpoint="https://uzair-resource-foundry-iq-1.search.windows.net",
    index_name="aisearch",
    credential=DefaultAzureCredential()
)

search_response = search_client.search(
    search_text= "get my money back?",
    select=["title"]
    )

for result in search_response:
    print(f"Score:  {result['@search.score']:.4f}")
    print(f"Source: {result['title']}")
    # print(f"Text:   {result['chunk']}")
    print("---")
