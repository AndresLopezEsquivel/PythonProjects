import os
import requests

PIXELA_USERNAME = os.environ.get("USERNAME")
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs"


"""
creating_user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=PIXELA_ENDPOINT, json=creating_user_params)
print(response.text)
"""

graph_headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

graph_config = {
    "id": "graph1",
    "name": "Reading",
    "unit": "min",
    "type": "int",
    "color": "momiji"
}

graph_response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=graph_headers)
print(graph_response.text)