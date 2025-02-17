import random

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if choose == 0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif choose == 1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif choose == 2:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
else:
    print("You typed an invalid number, you lose!")

rock_paper_scissors = [0 , 1 , 2]
computers_choose = random.choice(rock_paper_scissors)

print("Computer chose: ")

if computers_choose == 0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif computers_choose == 1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif computers_choose == 2:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
else:
    print("You typed an invalid number, you lose!")

if choose == 0 and computers_choose == 0:
    print("It's a draw ")
elif choose == 0 and computers_choose == 1:
    print("You lose")
elif choose ==0 and computers_choose == 2:
    print("You win!")
elif choose == 1 and computers_choose == 0:
    print("You win!")
elif choose == 1 and computers_choose == 1:
    print("It's a draw ")
elif choose == 1 and computers_choose == 2:
    print("You lose")
elif choose == 2 and computers_choose == 0:
    print("You lose")
elif choose == 2 and computers_choose == 1:
    print("You win!")
elif choose == 2 and computers_choose == 2:
    print("It's a draw ")
else:
    print("You chose the wrong number.")
