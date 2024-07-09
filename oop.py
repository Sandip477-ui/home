class Teacher:
    def __init__(self,name,salary):
        self.name= name
        self.salary= salary

    def display(self):
        print(f"name is :{self.name} \n salary is :{self.salary} ")
            

te1=Teacher(name="bikash",salary=10000)
te1.display()

te2=Teacher(name="sandip",salary=8000)
te2.display()

te3=Teacher(name="ram",salary=30000)
te3.display()

te4=Teacher(name="suman",salary=3500)
te4.display()
