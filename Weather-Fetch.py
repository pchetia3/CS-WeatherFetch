import requests
import time
import datetime

LOOKAHEAD_MINUTES = 20;
SECONDS_PER_MINUTE = 60;

INTERESTED_ATTRIBUTES = ["temperature", "humidity", "time", "summary"]

apikey = "ea67e9edd8f0a4f0e9c3fb6eec30591d"

#values used (New york): lat = "42.3601",long = "-71.0589"
latitude = input("Enter Latitude: ")
longitude = input("Enter longitude: ")
# now = str(datetime.datetime.now())
# print(now)
# time = "[" + now[:4:1] + "]-[" + now[5:7:1] + "]-[" + now[8:10:1] +"]T[" + now[11:13:1] + "]:[" + now[14:16:1] +"]:[" + now[17:19:1] + "][" + now[20:26:1]
address_api = "https://api.darksky.net/forecast/" + apikey + "/" + latitude + "," + longitude


#time_part
current_ts = time.time(); #current timestamp (same everywhere in the world)
lookahead_seconds = LOOKAHEAD_MINUTES * SECONDS_PER_MINUTE;

latter_time = current_ts + lookahead_seconds

address_api += "," + str(int(latter_time))

jsondata = requests.get(address_api).json()

print("\nWeather conditions in 20 minutes:")

for key in jsondata["currently"]:
    if key in INTERESTED_ATTRIBUTES:
        print(key + ": " + str(jsondata["currently"][key]))

#print(ts)



#format_d = jsondata["hourly"]["data"][0]["time"]


#print(format_d)
