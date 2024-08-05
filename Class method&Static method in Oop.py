# Class method and Static method  in OOP
#@classmethod
# @staticmethod
 
class PlayerCharacter:
    membership = True
    def __init__(self,name,age):
        self.name = name              #Attributes
        self.age = age      #Instance Variables

    def shout(self):
        print(f'My name is {self.name}')
       
    @classmethod
    def adding_things(cls,num1, num2):
        return cls('Teddy',num1 + num2)
    
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

# player1 = PlayerCharacter('Aswin',23)
# print(player1.adding_things(11,22))
# print(PlayerCharacter.adding_things(11,22))        
player3 = PlayerCharacter.adding_things(2,3)
print(player3.age)   


class NameOfClass:
    class_attribute = 'Value'
    
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method(self):
        # Regular instance method
        pass

    @classmethod
    def cls_method(cls, param1, param2):
        # Class method
        pass

    @staticmethod
    def stc_method(param1, param2):
        # Static method
        pass

            

#Static Method and static Members

class Person:

    sleepingtime = 8

    def __init__(self,name,age):
        self.name = name
        self.age = age
        # self.sleepingtime = 10
        sleepingtime = 10
    # @staticmethod
    # def Sleep():
    #     print('Person Should sleep for' ,Person.sleepingtime, 'Hours')

    # @classmethod
    # def Sleep(cls):
    #     print('Person Should sleep for' ,cls.sleepingtime, 'Hours')

    @classmethod
    def Sleep(cls):
        cls.Eat()

    def Eat(self):
        print(Person.sleepingtime)
# person1 = Person('Aswin',22)
# print(person1.sleepingtime)
# print(Person.sleepingtime)
# person1 = Person('Caleb',23)
# print(person1.sleepingtime)
Person.Sleep()