
romandic = {
            1:"I",
            4:'IV',
            5:"V",
            9:"IX",
            10:"X",
            40:"XL",
            50:"L",
            90:"XD",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M",
                    }
key_roman = []
value_roman = []
for i in romandic.keys():
    key_roman.append(i)
for i in romandic.values():
    value_roman.append(i)
key_roman = key_roman[::-1]
value_roman = value_roman[::-1]
class Integer_To_Roman:
    def __init__(self,num):
        self.n=num
    def change(self):   
        ans=""
        start = 0
        while self.n >0:
            for i in range(self.n//key_roman[start]):
                ans += value_roman[start]
                self.n -= key_roman[start]
            start += 1
        return ans
num = int(input("Enter an integer:\n"))
if num <= 0:
    print(f"The Roman numeral representation of {num} is Invalid input")
else:
    changeint = Integer_To_Roman(num)
    print(f"The Roman numeral representation of {num} is {changeint.change()}")