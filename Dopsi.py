class dopsi:
    def __init__(self):
        self.drivers = []
        self.passengers = []
        self.trips = []


    # add driver to driverslist
    def addDriver(self, driver):
        self.drivers.append(driver)

    # add passenger to passengers list
    def addPassenger(self, passenger):
        self.passengers.append(passenger)

    # add trip to trips list
    def addTrip(self, trip):
        self.trips.append(trip)

    # edit status of trips
    def editStatus(self, idTrip):
        for trip in self.trips:
            if trip.id == idTrip:
                trip.status = 1
                break

    # show all trips of a driver in specific time
    def showDriversTrips(self, driver, time):
        for d in self.drivers:
            if d.phoneNumber == driver.phoneNumber:
                for t in d.trips:
                    if t.date == time:
                        print(t.id)

    # show status of a specific passenger trips
    def showPassengersTrips(self, passenger):
        for p in self.passengers:
            if p.phoneNumber == passenger.phoneNumber:
                return
