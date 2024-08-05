#4 Pillars of OOP
#Encapsulation (Encapsulation is the binding of data and functions that manipulate that data)(Hiding the object which is to be Hidden)
#Public - None
#Private - __Private
#Protected - _Protected


class School:
    def __init__(self):
        self.Name = 'ABC'
        self.place = 'Ooty'
        self._Revenue = 500000        #__private Variable

    # def SchoolRevenue(self):           #Public method
    #     print(self.__Revenue)

# class Faculty(School):
#     def common(self):
#         pass
    # def __PrivateMethod(self):
    #     print(self.__Revenue)
    
    # def PublicMethod(self):
    #     self.__PrivateMethod()

class Faculty(School):
    
    def Revenue(self):
        print(self._Revenue)

# school1 = School()
# print(school1.Name)
# print(school1.__place)
# print(school1.__Revenue)
# school1.SchoolRevenue()
# print(school1._School__Revenue)
# print(school1.PublicMethod())
faculty1 = Faculty()
# faculty1.Revenue()
print(faculty1._Revenue)


#Getter & Setter(only for a Private Variable)

class Person:

    def __init__(self):
        self.__name = None
        self.__age = None

    #Getter (Always on top)
    @property
    def name(self):
        if self.__name is None:
            return "Please initialize Name"
        return self.__name           #Return Keyword is Mendatory&Always Recommended
    
    #setter
    @name.setter
    def name(self,Value):
        if len(Value) > 20:
            print("Can't set Name Character More than 20")
        else:
            self.__name = Value
#Outside the class
person1 = Person()
# person1.SetName('usddghudgsfdgsyfgyfsytjhsgfyg')
# person1.name = ("Hariharan")
person1.name = "Aswin"        #Setter
# print(person1.GetName())
print(person1.name)           #Getter
person1.age = 10
print(person1.age)


class Person:
    def __init__(self):
        self.__Firstname = "Hari"
        self.__Lastname = "haran"
    @property         #Method to Variable
    def FullName(self):
         return self.__Firstname + '' +self.__Lastname
        #print(f"{self.__Firstname}{self.__Lastname}")
person1 = Person()
print(person1.FullName)



class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name
        self.age = age                    #when ever self.name is Assigned as a Variable its called as Instance Variables

    # def run(self):
    #     print('run')

    # def speak(self):
    #     print(f'My name is {self.name} and Iam {self.age} Years old')

player1 = PlayerCharacter('Aswin',23)
# player1.speak()
print(player1.name)
print(player1.age)

player2 = {'name':'Hari','age':22}
print(player2['name'])
print(player2['age'])

