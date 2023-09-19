class car:
    def __init__(self,name,speed,mile):
        self.n=name
        self.s=speed
        self.m=mile
    def venhicle(self):
        a = f'Vehicle Name: {self.n} Speed: {self.s} Mileage: {self.m}'
        return a
name = input("Enter the bus name:\n")
speed = float(input("Enter the maximum speed of the bus:\n"))
mile = float(input("Enter the mileage of the bus:\n"))
car = car(name,speed,mile)
print(car.venhicle())