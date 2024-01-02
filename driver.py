import random

import Person
import main
import Passenger


class driver(Person.person):
    def __init__(self, firstName, lastName, phoneNumber, carModel, carTag, music, AC, licensee, specialNeeds):
        super(driver, self).__init__(firstName, lastName, phoneNumber)
        self.carModel = carModel
        self.carTag = carTag
        self.music = music
        self.AC = AC
        self.licensee = licensee
        self.specialNeeds = specialNeeds
        self.dates = []
        self.trips = []
        main.dopsii.addDriver(self)
        self.x = random.Random.randint()
        self.y = random.Random.randint()
        self.income = 0


    # checks the trip and accept
    def acceptTrip(self, trip):
        for t in self.trips:
            if t.date == trip.date:
                return 0
        for d in main.dopsii.drivers:
            if d.phoneNumber == self.phoneNumber:
                d.trips.append(trip)
                # add cost to income
                d.income += trip.cost
        trip.passenger.editTrip(trip.id, self)

    # show trips for driver
    def showTrips(self, start, end):
        for d in main.dopsii.drivers:
            if d.phoneNumber == self.phoneNumber:
                for t in d.trips:
                    if t.date >= start and t.date <= end:
                        print(t.id)
