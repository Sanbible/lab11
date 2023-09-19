# Accept user input for car details
car_make = input("Enter the car's make (manufacturer): ")
car_model = input("Enter the car's model: ")
car_year = int(input("Enter the car's year: "))
car_doors = int(input("Enter the number of doors in the car: "))
class Vehicle:
    def __init__(self,make,model,year):
        self.m = make
        self.md = model
        self.y = year
    def start_engine(self):
        return f"The {self.y} {self.m} {self.md}'s engine is now running."
    def stop_engine(self):
        return f"The {self.y} {self.m} {self.md}'s engine is now stopped."
# Create a Car object
class Car(Vehicle):
    def __init__(self,make,model,year,door):
        super().__init__(make,model,year)
        self.d=door
    def honk(self):
        return f"The {self.y} {self.m} {self.md} goes 'Honk! Honk!'"
car = Car(car_make, car_model, car_year, car_doors)

# Accept user input for motorcycle details
motorcycle_make = input("Enter the motorcycle's make (manufacturer): ")
motorcycle_model = input("Enter the motorcycle's model: ")
motorcycle_year = int(input("Enter the motorcycle's year: "))
motorcycle_has_kickstand = input("Does the motorcycle have a kickstand? (yes/no):\n").lower() == "yes"

# Create a Motorcycle object
class Motorcycle(Vehicle):
    def __init__(self,make,model,year,kickstand):
        super().__init__(make,model,year)
        self.k=kickstand
    def wheelie(self):
        if self.k :
            return  f"The {self.y} {self.m} {self.md} pops a wheelie!"
        else :
            return  f"The {self.y} {self.m} {self.md} can't do a wheelie without a kickstand."
car = Car(car_make, car_model, car_year, car_doors)
motorcycle = Motorcycle(motorcycle_make, motorcycle_model, motorcycle_year, motorcycle_has_kickstand)

# Example usage:
a=car.start_engine()
print(a)
a=car.honk()
print(a)
a=car.stop_engine()
print(a)
a=motorcycle.start_engine()
print(a)
a=motorcycle.wheelie()
print(a)
a=motorcycle.stop_engine()
print(a)