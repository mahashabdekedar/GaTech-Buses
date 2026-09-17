import requests
import time
from numpy.ma.core import size

# No buses running at time of test, need to run later.
url = "https://bus.gatech.edu/Services/JSONPRelay.svc/GetMapVehiclePoints?apiKey=8882812681&isPublicMap=true"

response = requests.get(url)
print("Status Code:", response.status_code)
print("Content Type", response.headers.get("Content-Type"))
data = response.json() # Get the JSON as a python dict
print(data[0])

# Find different route numbers
routeSet = set()
for d in data:
    routeSet.add(d['RouteID'])
print(routeSet)

# Pair buses to routes
nameToRoute = {}
for d in data:
    nameToRoute[d['Name']] = d['RouteID']

print(nameToRoute)
# Manually checking against transloc, we get the following Route IDs:
# 29: Gold
# 21: Blue
# 28: Clough
# 20: Red
# 18: Emory
# 26: Northside Dr. - Atlantic Station
# 17: Green

# Make sure we didn't get any other RouteIDs
for d in data:
    if (d['RouteID'] not in (29, 21, 28, 20, 18, 26, 17)):
        print(f"Unidentified route #{d['RouteID']}")
