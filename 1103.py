class Vehicle:
    def __init__(self,name, maximumspeed, mileage):
        self.n=name
        self.ma=maximumspeed
        self.m=mileage
class bus(Vehicle):
    def __init__(self,name, maximumspeed, mileage,passenger=50):
        super().__init__(name, maximumspeed, mileage)
        self.p=passenger
    def passen(self):
        return self.p
a = int(input("Enter the seating capacity of the bus:\n"))
schoolbus = bus("School Volvo",180,12,a)
print(f"The seating capacity of a School Volvo is {schoolbus.passen()} passengers")