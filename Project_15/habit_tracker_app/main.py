import requests
import datetime as dt

TOKEN="pixela_api_key"
USERNAME="danyanderson2222"
GRAPH="graph1"
# Based on the pixela API
pixela_endpoint = "https://pixe.la/v1/users"
pixela_parameters={
    "token": TOKEN,              # is made up at random, just like self generate api key
    "username": USERNAME,
    "agreeTermsOfService": 'yes',
    "notMinor": "yes"
}
# response=requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)
# -------------------------------Setting Graph ---------------------------------------------
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params={
    "id": GRAPH,
    "name": "Gym workout",
    "unit": "minutes",
    "type": "float",
    "color": "shibafu"
}
headers={
    "X-USER-TOKEN":TOKEN
}
graph_resp=requests.post(url=graph_endpoint, json=graph_params, headers=headers)

# ------------------------------ adding a pixel -------------------------------------------
today=dt.datetime.now().date()
# print(today)
pixel_fill_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
fill_params={
    "date": today.strftime("%Y%m%d"),
    "quantity": "75.0",
}
formatted=today.strftime("%Y%m%d")
print(formatted)
pixel_fill_resp=requests.post(url=pixel_fill_endpoint,json=fill_params,headers=headers)
print(pixel_fill_resp.text)

# ------------------------- Updating a pixel with put method ------------------
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{fill_params['date']}"
update_params={
    "quantity": "80"
}

responive=requests.put(url=update_endpoint, json=update_params, headers=headers)
print(responive.text)