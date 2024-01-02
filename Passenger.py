import Person
import Trip
import Dopsi
import main


class passenger(Person.person):
    def __init__(self, firstName, lastName, phoneNumber):
        super(passenger, self).__init__(firstName, lastName, phoneNumber)
        main.dopsii.addPassenger(self)
        self.trips = []
        self.status = 0

    # new trip
    def newTrip(self, xs, ys, xe, ye, music, AC, licensee, specialNeeds, passenger):
        t = Trip.trip(xs, ys, xe, ye, music, AC, licensee, specialNeeds, passenger, None)
        # add trip to passenger trips list
        for p in main.dopsii.passengers:
            if p.phoneNumber == self.phoneNumber:
                p.trips.append(t)
                p.status = 1
        # add trip to dopsi trips list
        main.dopsii.addTrip(Trip.trip(t))

    # edit status of trip for passenger
    def editTrip(self, id, driver):
        for p in main.dopsii.passengers:
            if p.phoneNumber == self.phoneNumber:
                for t in p.trips:
                    if t.id == id:
                        t.status = True
