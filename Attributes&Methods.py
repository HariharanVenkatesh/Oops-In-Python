class PlayerCharacter:
    #Class object Attribute
    membership = True
    def __init__(self,name,age):
      if (PlayerCharacter.membership): 
        self.name = name              #Attributes
        self.age = age


    # def run(self):
    #     print('run')
    #     return 'done'


    def shout(self):
        print(f"My name is {self.name}")

    def run(self,Hello):
        print(f"My name is {self.name}")

player1 = PlayerCharacter("Hariharan",22)            #instanciate
player2 = PlayerCharacter("Aswin",23)
player3 = PlayerCharacter("Caleb",23)
player4 = PlayerCharacter("Abi",23)
player5 = PlayerCharacter("Pradeep",23)
player2.attack = 24

  
# print(player1.name)
# print(player2.name)
# print(player3.name)
# print(player4.name)
# print(player5.name)
# print(player1.run())
# print(player1.age)
# print(player1)
# print(player2)
# print(player2.attack)
# print(player1.membership)
# print(player1.shout())
# print(player2.shout())
# print(player3.shout())
# print(player4.shout())
# print(player5.shout())
# print(player1.run("Hello"))