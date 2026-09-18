import requests
import numpy as np

from src.route_id import Constants

currLat = 0
currLong = 0
while True:
    data = requests.get(Constants.url).json()[0]
    if currLat != data['Latitude'] or currLong != data['Longitude']:
        myHeading = np.degrees(np.arctan2(data['Longitude'] - currLong, data['Latitude'] - currLat)) % 360

        print(f"My Heading: \t{myHeading}")
        print(f"Transloc Heading: \t{data['Heading']}")

        currLong = data['Longitude']
        currLat = data['Latitude']