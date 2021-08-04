import json
import requests

# ----------- Codes -------------#
#   1XX: Hold ON
#   2XX: Here you go (success)
#   3XX: Go away (not enough permissions)
#   4XX: You fucked up so badly.
#   5XX: I screwed up so badly ( Server problem)


response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response) #printing response code
print(response.status_code)
response.raise_for_status()

data = response.json()
position = response.json()["iss_position"]
longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

print(json.dumps(data, indent=2), "\n")
print(json.dumps(position, indent=2), "\n")
print(json.dumps(longitude, indent=2))
print(json.dumps(latitude, indent=2))

#Creating tuple of location
iss_position = (longitude,latitude)
print(iss_position)

