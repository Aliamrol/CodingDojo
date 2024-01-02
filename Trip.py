import datetime
import KATA
import main


class trip:
    def __init__(self, xs, ys, xe, ye, music, AC, licensee, specialNeeds, passenger, driver):
        self.xs = xs
        self.ys = ys
        self.xe = xe
        self.ye = ye
        self.licensee = licensee
        self.specialNeeds = specialNeeds
        self.music = music
        self.AC = AC
        self.passenger = passenger
        self.driver = driver
        self.status = False
        self.date = datetime.datetime.now()
        self.id = datetime.datetime.now().microsecond
        self.cost = KATA.calculateCost(xs, ys, xe, ye)
        self.option = 0
        self.plus = 0
        if self.music == 1:
            self.option += 1
            self.plus += self.cost * 0.05
        if self.specialNeeds == 1:
            self.option += 1
            self.plus += self.cost * 0.2
        if self.licensee == 1:
            self.option += 1
            self.plus += self.cost * 0.1
        if self.AC == 1:
            self.option += 1
            self.plus += self.cost * 0.15
