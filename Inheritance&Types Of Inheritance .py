#Inheritance(Inheritace allows new objects to take on the properties of Existing Objects so you can inherit classes)
#Users
#Inheritance in Python
#Types of Inheritance 
        # Single Inheritance
        # Multiple inheritance
        # Multilevel inheritance
        # Hierarchical inheritance
        # Hybrid inheritance

#Before Inheritance
class Human:
    def eat(self):
        print("I can Eat")
    def work(self):
        print("I can Work")
class Male:
    def eat(self):
        print("I can Eat")
    def work(self):
        print("I can Work")
male_1 = Male()
male_1.eat()

#After Inheritance (Main purpose of inheritance is to increase the Reusability of the code) 
#Single inheritance

class Human:
    def __init__(self,no_hands):
        self.no_eyes = 2
        self.no_nose = 1
        self.no_hands = no_hands
    def eat(self):    
        print("I can Eat")
    def work(self):
        print("I can Work")
class Male(Human):
    def __init__(self,name,hands):
       super().__init__(hands)
       self.name = name
    def Drive(self):
        print("I can Drive")
    def work(self):
        super().work()
        print("I can Code")    #OverRiding
    def display(self):
            print(f"Hi,I am {self.name} and I have {self.no_hands} Hands.")
male_1 = Male("Caleb",2)
# male_1.Drive()
# male_1.work()
print(male_1.no_eyes)
print(male_1.name)
print(male_1.no_hands)
male_1.display()



class User(object):
    def sign_in(self):
        print('Logged in')

class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power 
        
    def attack(self):
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self,name,no_of_arrows):
        self.name = name
        self.no_of_arrows =  no_of_arrows
        
    def attack(self):
        print(f'Attacking with arrows: arrows left- {self.no_of_arrows}')

wizard1 = Wizard('Hariharan',50)
# archer1 = Archer('Aswin',500)
# print(wizard1.sign_in())
# wizard1.attack()
# archer1.attack()

print(isinstance(wizard1,object))



#Multilevel Inheritance

class GrandParent:
    def swim(self):
        print("Swimming")
    
class Parent(GrandParent):

    def __init__(self):
        self.Networth = 1000000

    def Sing(self):
        print('Parent is Singing')

class Child(Parent):

    def Dance(self):
        print("Child is Dancing")

chlid1 = Child()
chlid1.Sing()
chlid1.Dance()
print(chlid1.Networth)

#Singlelevel Inheritance

class Parent():

    def __init__(self):
        self.Networth = 1000000

    def Sing(self):
        print('Parent is Singing')

class Child(Parent):

    def Dance(self):
        print("Child is Dancing")

#Multiple Inheritance

class GrandParent:
    def swim(self):
        print("Swimming")
    
class Parent:

    def __init__(self):
        self.Networth = 1000000

    def Sing(self):
        print('Parent is Singing')

class Child(Parent,GrandParent):

    def Dance(self):
        print("Child is Dancing")

# child1 = Child()
parent1 = Parent()
parent1.Sing

#Multiple Inheritance in Python

class Human:
    def __init__(self,no_hands):
        print("Calling init from Human")
        self.no_eyes = 2
        self.no_nose = 1
        self.no_hands = no_hands
    def Eat(self):
        print("I can Eat")
    def work(self):
        print("I can Work")

class Male:
    def __init__(self,language):
        ("Calling init from Male")
        self.language = language
    def Drive(self):
        print("I can Drive")
    def work(self):
        print("I can Code")

# class Boy(Human,Male):
#     pass

# class Boy(Male,Human):
#     pass


class Boy(Human,Male):
    def __init__(self,name,language):
        Human.__init__(self)
        Male.__init__(self,name)
    def sleep(self):
        print("I can Sleep")
    def work(self):
        print("I can Test")         

boy_1 = Boy("Aswin")
# boy_1.Drive()
# boy_1.work()
#  Male.work(boy_1)
# Boy.mro()                         #mro - Method resolution Order
# print(Boy.mro())
print(boy_1.no_nose)
# print(boy_1.name)


#Hierarchical Inheritance

class GrandParent:
    def swim(self):
        print("Swimming")
    
class Parent(GrandParent):

    def __init__(self):
        self.Networth = 1000000

    def Sing(self):
        print('Parent is Singing')

class Child(GrandParent):

    def Dance(self):
        print("Child is Dancing")


#Hybrid Inhritance(Combination of Single level,Multilevel,Multiple,Hierarchical Inheritance)

class GrandParent:
    def swim(self):
        print("Swimming")

class Relative(GrandParent):
    def Drive(self):
        print('Driving')
    
class Parent(GrandParent):

    def __init__(self):
        self.Networth = 1000000

    def Sing(self):
        print('Parent is Singing')

class Child(Parent,Relative):

    def Dance(self):
        print("Child is Dancing")


# Multiple Inheritance & Super Keyword

class Parent:
    def  Drive(self,Speed):
        print('Parent is Driving at the speed of',Speed)

class  Child(Parent):
    def Drive(self,Speed):
        super().Drive(Speed)
        print('Child is Driving at the speed of',Speed - 40)


child1 = Child()
child1.Drive(70)


class Parent:
    def  __init__(self,Networth):
        self.Networth = Networth

class  Child(Parent):
    def __init__(self,Networth):
        super(). __init__(Networth)
        print("Child constructor is Invoked")

    def ChildNetworth(self):
        print(self.Networth//2)

child1 = Child(1000000)
# print(child1.ChildNetworth())
print(child1. Networth)
child1.ChildNetworth()

#Multiple Inheritance ,Super,mro

class GrandParent:
    def Swim(self):
        print('Swimming')

class Parent:
    def sing(self):
        print('Parent is Singing')

class Relative:
    def Drive(self):
        print('Driving')

    def sing(self):
        print('Relative is Singing')

class Child(Parent,Relative):
    def Common(self):
        super(Parent,self).sing()
        pass

    def sing(self):
        print('Relative is Singing')


# print(Child.__mro__)
# print(Child.mro())
child1 =  Child()
# Relative.sing(child1)
Child.Common(child1)

#Multiple Inheritance

class User(object):
    def sign_in(self):
        print('Logged in')

class wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self,name,arrows):
        self.name = name 
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def run(self):
        print('Ran Really Fast')

class HybridBorg(wizard,Archer):
    def __init__(self,name, power, arrows):
        Archer.__init__(self,name,arrows)
        wizard.__init__(self,name,power)

hb1 = HybridBorg('Hariharan',50,100)
# print(hb1.run())
# print(hb1.check_arrows())
# print(hb1.attack())       
print(hb1.sign_in())


#MRO - Method Resolution Order

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B,C):
    pass 

# print(D.num)
print(D.mro())


class X:pass
class Y:pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z):pass

print(M.__mro__)
