import requests

from src.bus import Bus, FleetManager
from src.route_id import Constants

fm = FleetManager(requests.get(Constants.url).json())
while True:
    data = requests.get(Constants.url).json()
    fm.update(data)
    print(fm.buses)
