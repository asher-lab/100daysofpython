import requests
import datetime as dt


PIKELA_TOKEN = "Scabaluda@@2800"
PIXELA_UNAME = "asher"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIKELA_TOKEN,
    "username": PIXELA_UNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Creating user
#   response = requests.post(url=pixela_endpoint, json=user_params)
#   print(response.text)

graph_endpoint = f"{pixela_endpoint}/{PIXELA_UNAME}/graphs"

#Making post request
user_params_graph = {
    "id": "asher1",
    "name": "Asher Habits",
    "unit": "study",
    "type": "int",
    "color": "shibafu"
}


#Making X HEADER Authentication token

header = {
    "X-USER-TOKEN": PIKELA_TOKEN
}
response = requests.post(url=graph_endpoint, json=user_params_graph, headers = header)
print(response.text)

# ----- https://pixe.la/v1/users/asher/graphs/asher1.html


pixel_creation_endpoint = f"{pixela_endpoint}/{PIXELA_UNAME}/graphs/asher1"
print(pixel_creation_endpoint)
today = dt.datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study todayy? ")
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=header)
print(response.text)


# put method / put is also known as updating the data
update_endpoint = f"{pixela_endpoint}/{PIXELA_UNAME}/graphs/asher1/{today.strftime('%Y%m%d')}"
pixel_update = {
    #"date": today.strftime("%Y%m%d"),
    "quantity": input("Change hrs? ")
}

#   response = requests.put(url=update_endpoint, json=pixel_update, headers=header)
#   print(response.text)


#delete endpoint

#   delete_endpoint = f"{pixela_endpoint}/{PIXELA_UNAME}/graphs/asher1/{today.strftime('%Y%m%d')}"
#   response = requests.delete(url=delete_endpoint, headers=header)
#   print(response.text)
