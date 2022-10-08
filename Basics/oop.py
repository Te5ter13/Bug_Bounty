#Demonstration of OOP

class Student:
    def __init__(self,first,last,pay):
        self.firstname=first
        self.lastname=last
        self.payment=pay

    def salary(self):
        return self.payment*100

stud1=Student("Iphone","Thirteen",10)

print(stud1.salary())