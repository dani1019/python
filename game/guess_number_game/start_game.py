import random
easy_attempt_num = 10
hard_attempt_num = 5

#ゲームスタートしゲームレベルを選択する
def start_question():
    print("welcome to the Number Guessing Game!\n"
    "I'm thinking of a number between 1 and 100")
    
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        print(f"You have {easy_attempt_num} attempts remainging to guess the number.")
    elif level == "hard":
        print(f"You have {hard_attempt_num} attempts remainging to guess the number.")

    #数字をランダムに選択する
    random_number= random_select_number()

    #予想あれる数字を入力する
    make_a_guess(random_number)

def random_select_number():
    random_number = random.randint(1, 100)
    print(f"answer: {random_number}")
    return random_number
    
    #予想あれる数字を入力する
def make_a_guess(random_number):
    right_check = False
    while not right_check:
        enter_number = int(input("Make a guess: "))
        if enter_number < random_number:
            print("Too Low")
        elif enter_number > random_number:
            print("Too high")
        else:
            print(f"You got it! The answer was {random_number}")
            right_check = True