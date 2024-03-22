from dotenv import load_dotenv
from datetime import datetime
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

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }
#
headers = {
    "X-USER-TOKEN": PIXELA_SECRET
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{"graph1"}"
today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "13.3"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{"graph1"}/{today.strftime("%Y%m%d")}"
new_pixel_data = {
    "quantity": "10"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{"graph1"}/{today.strftime("%Y%m%d")}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
