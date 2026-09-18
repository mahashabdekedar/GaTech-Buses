import numpy as np
import time


class Bus:

    def __init__(self, data:dict):
        # What does a bus really need?
        # Route number, bus number, longitude latitude... time last updated?

        self.latitude = data['Latitude']
        self.longitude = data['Longitude']
        self.routeId = data['RouteID']
        self.busID = data['Name']
        self.heading = None # Where 0 is north, 90 is east, 180 is south, and 270 is west
        self.updateTime = time.perf_counter()


    def updateposition(self, newLong:int, newLat:int):
        self.heading = np.degrees(np.arctan2(newLat - self.latitude, newLong - newLong)) % 360
        self.longitude = newLong
        self.latitude = newLat
        self.updateTime = time.perf_counter()

class FleetManager:
    def __init__(self, data:list):
        # Map of bus id to bus object
        self.buses = dict()
        for d in data:
            self.buses[d['Name']] = Bus(d)


    def update(self, data:list):

        listed = set()
        # Update all buses in the response
        for d in data:
            if self.buses.__contains__(d['Name']):
                self.buses[d['Name']].updateposition(d['Longitude'], d['Latitude'])
            else:
                self.buses[d['Name']] = Bus(d)
            listed.add(d['Name'])

        # Remove all buses not in the response
        for busId in self.buses:
            if not listed.__contains__(busId):
                self.buses.pop(busId)