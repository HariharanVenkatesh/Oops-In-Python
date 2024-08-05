#Polymorphism(Many Forms)&Super
#Compile Time - Method name will be same but passing parameters count or type will be change(Method Overloading)
#Run time - Over 
#Python is a Dynamically typing language

#Compile Time polymorphism
class Person:

    def __init__(self,name,age):
        self.Name = name
        self.Age = age

    def Sleep(self,sleepingHours = None,start = None,end = None):

        if start is not None and end is not None:
            print('Sleeping Duration is',abs(end - start),'Hours')           #Here abs stands for absolute value its converts -ve value to +ve value
        else:    
            print('Sleeping Duration is',sleepingHours,'Hours')

    # def Sleep(self,Start,End):                                        #Method Overloading
    #     print('Sleeping Duration is',End - Start,'Hours')

person1 = Person('Hariharan',22)
# person1.Sleep(10)
person1.Sleep(start = 20,end = 6)

#Runtime Polymorphism

class Parent:
    def Drive(self):
        print("Parent is Driving")

class Child(Parent):
    def Drive(self):
        print("Child is Driving")

# child1 = Child()
# child1.Drive()
obj = None
name = input()
if name == "Parent":
    obj = Parent()
else:
    obj =   Child()

obj.Drive()




class User(object):
    def __init__(self,email):
        self.email = email

    def sign_in(self):
        print('Logged in')

    def attack(self):
        print('Do Nothing')

class Wizard(User):
    def __init__(self,name,power,email):
        # User.__init__(self,email)
        super().__init__(email)
        self.name = name
        self.power = power 
        
        
    def attack(self):
        User.attack(self)
        print(f'Attacking with power of : {self.power}')

class Archer(User):
    def __init__(self,name,no_of_arrows):
        self.name = name
        self.no_of_arrows =  no_of_arrows
        
    def attack(self):
        print(f'Attacking with arrows: arrows left : {self.no_of_arrows}')

wizard1 = Wizard('Caleb',60)
archer1 = Archer('Abi',30)

def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)

for char in [wizard1,archer1]:
    char.attack()

print(wizard1.attack())
print(wizard1.sign_in())
wizard1 = Wizard('Pradeep',60,'Pradeep@gmail.com')
print(wizard1.email)

