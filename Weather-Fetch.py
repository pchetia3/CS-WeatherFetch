import requests
import datetime

apikey = "ea67e9edd8f0a4f0e9c3fb6eec30591d"

latitude = input("Enter Latitude: ")
longitude = input("Enter longitude: ")
# now = str(datetime.datetime.now())
# print(now)
# time = "[" + now[:4:1] + "]-[" + now[5:7:1] + "]-[" + now[8:10:1] +"]T[" + now[11:13:1] + "]:[" + now[14:16:1] +"]:[" + now[17:19:1] + "][" + now[20:26:1]
address_api = "https://api.darksky.net/forecast/"+ apikey +"/" +latitude + ","
+ longitude
jsondata = requests.get(address_api).json()
format_d = jsondata["hourly"]["data"][0]["time"]
print(format_d)


