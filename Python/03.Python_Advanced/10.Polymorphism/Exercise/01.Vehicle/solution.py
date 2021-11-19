from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        self.fuel_consumption += 0.9
        if self.fuel_consumption * distance <= self.fuel_quantity:
            self.fuel_quantity -= (self.fuel_consumption * distance)
            return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel
        return self.fuel_quantity


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        self.fuel_consumption += 1.6
        if self.fuel_consumption * distance <= self.fuel_quantity:
            self.fuel_quantity -= (self.fuel_consumption * distance)
            return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel - (fuel * 0.05)
        return self.fuel_quantity