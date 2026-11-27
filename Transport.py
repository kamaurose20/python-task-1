# Parent Class
class Vehicle:
    def __init__(self, registration_number, model):
        self.registration_number = registration_number
        self.model = model

    def displayVehicle(self):
        print("Registration Number:", self.registration_number)
        print("Model:", self.model)


# Child Class
class Bus(Vehicle):
    def __init__(self, registration_number, model, passenger_capacity):
        super().__init__(registration_number, model)
        self.passenger_capacity = passenger_capacity

    def displayBus(self):
        print("Registration Number:", self.registration_number)
        print("Model:", self.model)
        print("Passenger Capacity:", self.passenger_capacity)


# Main Program
bus = Bus("KDA 123A", "Scania", 52)

bus.displayBus()