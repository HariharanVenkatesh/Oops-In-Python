#Abstraction(Hiding of information or abstracting away information and giving access to only what's necessary)

class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def run(self):
        print('run')

    def speak(self):
        print(f'My name is {self.name} and Iam {self.age} Years old')

player1 = PlayerCharacter('Hariharan',22)
player1.name = '!!!'
player1.speak = 'Booo'
# print((1,2,3,1).count(1))
print(len((1,2,3,1)))

print(player1.speak)

#Hiding Implementation Details&Showing Only Necessary Informations

from abc import ABC,abstractmethod

class Vehicle(ABC):#Abstract Base Class
   def __init__(self):
    self._Name = "Vehicle"
    
    @property
    @abstractmethod
    def Name(self):
       pass

    @abstractmethod
    def startEngine(self):
        pass

    def Brake(self):
        print("Brake")

class Cars(Vehicle):
    def __init__(self):
       self.Model = "2010"
       super(). __init__()

    def StartEngine(self):
        # super(). __init__()
        print("Car Engine Started")
    
    @property
    def Name(self):
       return self._Name

car1 = Cars()
# car1.StartEngine()
# car1.Brake()
print(car1.Name)