from car import Car
import random

class UnreliableCar(Car):
    
    
    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability
        
    def drive(self, distance):
        """Attempt to drive the car a given distance based on reliability."""
        chance = random.uniform(0, 100)
        if chance < self.reliability:
            return super().drive(distance)
        else:
            return 0


    
