#Constructor
 
class Person:
    Name = None 

    def __init__(self,name,age,ph_no):
        self.Name = name
        self.Age = age
        self.No = ph_no

    def __init__(self,name):             #This is called as Constructor Overloading
        self.Name = name 

person1 = Person('Hariharan',22,6123465432)
print(person1.Name)
print(person1.Age)
print(person1.No)

person2 = Person('Aswin',22,6798013241)
print(person2.Name)
print(person1.Age)
print(person1.No)

# person2 = Person()
# person2.Name = 'Aswin'