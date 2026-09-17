import requests
import time

# Check how long it takes to get a response

url = "https://bus.gatech.edu/Services/JSONPRelay.svc/GetMapVehiclePoints?apiKey=8882812681&isPublicMap=true"

startTime = time.perf_counter()
try:
    data = requests.get(url)
except:
    print("Issue with request")
else:
    endTime = time.perf_counter()
    print(f"Response time: {endTime - startTime} seconds")