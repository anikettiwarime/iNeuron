# 7. Write a python program to create a Laptop class with 4 attributes(brand, ram, cpu, hdd)
# and 2 methods(showConfig() to print the values,  __init__() to initialize the values).
class Laptop:
    def __init__(s):
        s.brand = "Hp"
        s.ram = 8
        s.cpu = "i5 10gen"
        s.hdd = "512 gb"

    def __repr__(self):
        return (self.brand + " " + str(self.ram)+" " + self.cpu + " " + self.hdd)

    def showConfig(self):
        print("Brand :", self.brand)
        print("Ram :", self.ram)
        print("CPU :", self.cpu)
        print("Hdd :", self.hdd)


l = Laptop()

l.showConfig()
