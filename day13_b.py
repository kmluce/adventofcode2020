import fileinput

class BusSchedule():
    def __init__(self):
        self.leaveTime = 0
        self.frequencies = []
        self.closestTime = 0
        self.closestBus = 0
        self.timeSchedule = []
        self.buses = []
        self.busOffsets = []
        self.maxBusIndex = 0
        self.baseTime=0          # for holding the time t that we're currently checking
        self.testMultiple = 1    # testing the multiple of max bus

    def print_schedule(self):
        print("time is:", self.leaveTime)
        for element in self.frequencies:
            print(element)

    def initialize_schedule(self):
        for i, element in enumerate(self.frequencies):
            if element == 'x':
                pass
            else:
                #print(" element is ", element)
                self.buses.append(int(element))
                self.busOffsets.append(i)
                if int(element) >= self.buses[self.maxBusIndex]:
                    self.maxBusIndex = len(self.buses) - 1
                #print("max bus is ", self.buses[self.maxBusIndex])

    def input_schedule(self):
        for line in fileinput.input():
            if fileinput.isfirstline():
                line = line.rstrip()
                self.leaveTime = int(line)
            else:
                line = line.rstrip()
                self.frequencies = line.split(',')
        self.print_schedule()
        self.initialize_schedule()

    def test_bus_schedules(self):
        match = True
        lastMatch = 0
        timeIncrement = self.buses[0]
        print("offset for bus ", self.buses[0], " is ", self.busOffsets[0])
        for i, bus in enumerate(self.buses):
            print(" Testing", bus, "with increment", timeIncrement, "starting at base time", self.baseTime)
            if i == 0:
                continue
            while True:
                self.baseTime += timeIncrement
                print("  Testing to see if", self.baseTime, "+ offset", self.busOffsets[i], "mod", bus, "==0")
                if (self.baseTime + self.busOffsets[i]) % bus == 0:
                    timeIncrement *= bus
                    break
        print("Found result at time", self.baseTime)



if __name__ == '__main__':
    schedule = BusSchedule()
    schedule.input_schedule()
    schedule.test_bus_schedules()