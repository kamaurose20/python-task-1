# Parent Class
class Vehicle:
    def calculateFare(self, distance):
        pass


# Child Class
class Bus(Vehicle):
    def calculateFare(self, distance):
        return distance * 50


# Child Class
class Taxi(Vehicle):
    def calculateFare(self, distance):
        return distance * 100


# Main Program
distance = 10

bus = Bus()
taxi = Taxi()

print("Bus Fare: KSh", bus.calculateFare(distance))
print("Taxi Fare: KSh", taxi.calculateFare(distance))
