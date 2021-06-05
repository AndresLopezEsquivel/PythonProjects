import datetime
import os
import requests

# Visit to see the results: https://pixe.la/v1/users/arthurdent/graphs/graph1.html
DATE = datetime.datetime.now().date().strftime("%Y%m%d")
GRAPH_ID = "graph1"
PIXELA_USERNAME = os.environ.get("USERNAME")
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
CREATING_GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs"
POSTING_PIXEL_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"
UPDATING_PIXEL_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{DATE}"
DELETING_PIXEL_ENDPOINT = UPDATING_PIXEL_ENDPOINT


# CREATING A NEW USER
creating_user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=PIXELA_ENDPOINT, json=creating_user_params)
print(response.text)

# CREATING A NEW GRAPH
graph_headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading",
    "unit": "min",
    "type": "int",
    "color": "momiji"
}

graph_response = requests.post(url=CREATING_GRAPH_ENDPOINT, json=graph_config, headers=graph_headers)
print(graph_response.text)

# POSTING A PIXEL
posting_pixel_headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

minutes_read = 50

posting_pixel_params = {
    "date": DATE,
    "quantity": f"{minutes_read}",
}

graph_response = requests.post(url=POSTING_PIXEL_ENDPOINT,
                               json=posting_pixel_params,
                               headers=posting_pixel_headers)
print(graph_response.text)

# UPDATING AN EXISTING PIXEL
updating_pixel_headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

new_value_of_minutes_read = 120

updating_pixel_params = {
    "quantity": f"{new_value_of_minutes_read}",
}

graph_response = requests.put(url=UPDATING_PIXEL_ENDPOINT,
                              json=updating_pixel_params,
                              headers=updating_pixel_headers)

print(graph_response.text)

# DELETING PIXEL FROM GRAPH

updating_pixel_headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

response = requests.delete(url=DELETING_PIXEL_ENDPOINT, headers=updating_pixel_headers)
print(response.text)