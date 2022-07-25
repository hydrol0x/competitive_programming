"""
ID: mrjacob1 
LANG: PYTHON3
TASK: gift1 
"""

program_name = "gift1"

class Person:
   def __init__(self, name):
       self.account = 0
       self.name = name
   
   def addBalance(self, money):
      self.account+=money

with open(f'{program_name}.in', 'r') as fin:
    NP = int(fin.readline().strip())
    print(NP)
    friends = []
    for friend in range(NP):
      friends.append(Person(str(fin.readline().strip())))
    for line in fin:
      giver = Person(fin.readline().strip())
      gift, num_people = map(int, fin.readline().strip().split())
      recievers = []
      if len(recievers):
        giver.addBalance(int(gift/len(recievers)))
      else:
        giver.addBalance(gift)
      for reciever in range(num_people): 
        recievers.append(reciever)
      for reciever in recievers:
        for friend in friends:
          if str(friend.name) == str(reciever):
            friend.addBalance(gift % len(recievers))
for friend in friends:
  print(friend.account)