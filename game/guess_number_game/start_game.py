easy_attempt_num = 10
hard_attempt_num = 5

#ゲームスタートしゲームレベルを選択する
def start_question():
    print("welcome to the Number Guessing Game!\n"
    "I'm thinking of a number between 1 and 100")
    
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    #予想あれる数字を入力する
    select_level(level)

def select_level(level):
    if level == "easy":
        print(f"You have {easy_attempt_num} attempts remainging to guess the number.")
    elif level == "hard":
        print(f"You have {hard_attempt_num} attempts remainging to guess the number.")
