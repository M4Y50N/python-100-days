from dotenv import load_dotenv
import requests
import os

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"
PIXELA_SECRET = os.getenv("PIXELA_SECRET")
USERNAME = "seuotacilio"

# user_params = {
#     "token": PIXELA_SECRET,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": PIXELA_SECRET
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

print(response.text)
