class Vehicle:
    def __init__(self,name,mileage ):
        self.n=name
        self.m=mileage
        
class bus(Vehicle):
    def __init__(self,name,mileage ,seat ):
        super().__init__(name,mileage)
        self.s=seat
    def price(self):
        price=self.s*100*1.1
        return price
a=input("Enter the bus name:\n")
b=float(input("Enter the mileage of the bus:\n"))
c=float(input("Enter the seating capacity of the bus:\n"))
bus = bus(a,b,c)
print(f"Total Bus fare is: {bus.price}")