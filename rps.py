import random

print(" Welcome to Rock , Paper , Scissor Game!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

papper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissor = ''' 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

user_list = [rock, papper, scissor]
user = int(input("Choose one! 0 for Rock , 1 for Paper & 2 for Scissor:\n"))
if user >= 3 or user < 0:
    print("invalid number!")
else:
    print("user chose:")
    print(user_list[user])

    cpu = random.randint(0, 2)
    print("computer chose:")
    print(user_list[cpu])

    if user == 0 and cpu == 2:
        print("you win!")
    elif cpu == 0 and user == 2:
        print("you lose")
    elif cpu > user:
        print("you lose")
    elif user > cpu:
        print("you win!")
    elif cpu == user:
        print("it's a draw!")