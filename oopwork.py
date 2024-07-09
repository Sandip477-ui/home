class Laptop:
    def __init__(self,name,id,ram,price):
        self.name = name
        self.id = id
        self.ram = ram
        self.price = price

    def display(self):
        print(f"name is {self.name}\n id is :{self.id} ram is :{self.ram} price is:{self.price}")
lap1 = Laptop(name="apple",id="s213456",price="90000",ram="16gb")

lap2 = Laptop(name="samsung",price="80000",id="notebook",ram="32gb")
lap3 = Laptop(name="lenivo",id="d3456",price="200000",ram="512gb")
lap1.display()
lap2.display()
lap3.display()


