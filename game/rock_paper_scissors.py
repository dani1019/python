import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#ユーザー側入力
user_choice = int(input("What do you choice? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#ユーザーが選択したもの出力
if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
else:
  print(scissors)
print("Computer choice:")
case_list = [rock, paper, scissors]

#コンピューターの選択
computer_choice = random.randint(0,2)
print(case_list[computer_choice])

#ユーザー or コンピューター　どっちらが勝ったのか判断する
#user_choice[0] < computer[0] draw 
#user_choice[0] < computer[1] lose 
#user_choice[0] > computer[2] win  1
#user_choice[1]  > computer[0] win  1
#user_choice[1]  > computer[1] draw
#user_choice[1]< computer[2] lose 
#user_choice[2] < computer[0] lose 1
##user_choice[2] > computer[1] win  1
#user_choice[2]< computer[2] draw

#user_choice[0] > computer[2] win
if user_choice == 0 and computer_choice == 2:
  print("You win")
#user_choice[2] < computer[0] lose
elif user_choice == 2 and computer_choice == 0:
  print("You lose")
#user_choice[1]  > computer[0] win
##user_choice[2] > computer[1] win
elif  user_choice > computer_choice:
  print("You win")
elif  user_choice == computer_choice:
  print("It's draw")
#user_choice[0] < computer[1] lose
#user_choice[1]< computer[2] lose 
else:
  print("It's lose")