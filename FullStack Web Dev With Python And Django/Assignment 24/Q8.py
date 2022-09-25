# 8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted order based on the ram size.

class Laptop:
    def __init__(s):
        s.brand = "Hp"
        s.ram = 8
        s.cpu = "i5 10gen"
        s.hdd = "512 gb"

    def __repr__(self):
        return ("\n" + self.brand + " " + str(self.ram)+" " + self.cpu + " " + self.hdd + "\n")

    def showConfig(self):
        print("Brand :", self.brand)
        print("Ram :", self.ram)
        print("CPU :", self.cpu)
        print("Hdd :", self.hdd)


l1 = Laptop()
l2 = Laptop()
l3 = Laptop()

l1.ram = 10
l3.ram = 15
l2.ram = 12


list1 = [l1, l2, l3]


l1 = sorted(list1, key=lambda x: x.ram)

print(l1)
