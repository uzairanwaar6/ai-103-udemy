from openai import OpenAI
import os
import base64
import pathlib



endpoint = "https://uzair-anwaar-6-2499-resource.openai.azure.com/openai/v1"
deployment_name = "gpt-image-2"
api_key = "9WfKkdPOmW2WYMxkJSPBtW3ORxT6gI1YoJ5KAWH3zP8B4jzTNBFgJQQJ99CHACHYHv6XJ3w3AAAAACOGspm4"

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

input_image =pathlib.Path( "router.png")
output_image =pathlib.Path( "router_modified.png")

with input_image.open("rb") as file:
    response =client.images.edit(
        image=file,
        model=deployment_name,
        prompt="Replace router with Computer",
        quality="low",
        )


image = response.data[0].b64_json
output_image.write_bytes(base64.b64decode(image))