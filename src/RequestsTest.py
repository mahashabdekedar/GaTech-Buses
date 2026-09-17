import requests
from numpy.ma.core import size

# No buses running at time of test, need to run later.
url = "https://bus.gatech.edu/Services/JSONPRelay.svc/GetMapVehiclePoints?apiKey=8882812681&isPublicMap=true"

response = requests.get(url)
print("Status Code:", response.status_code)
print("Content Type", response.headers.get("Content-Type"))
data = response.json() # Get the JSON as a python dict
print()