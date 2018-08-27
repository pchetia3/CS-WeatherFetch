import requests

apikey = "ea67e9edd8f0a4f0e9c3fb6eec30591d"

latitude = input("Enter Latitude: ")
longitude = input("Enter longitude: ")
address_api = "https://api.darksky.net/forecast/"+ apikey +"/" +latitude + ","+ longitude
jsondata = requests.get(address_api).json()
print(jsondata)


