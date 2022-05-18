import random
remain_chance = 0

#ゲームスタートしゲームレベルを選択する
def start_question():
    print("welcome to the Number Guessing Game!\n"
    "I'm thinking of a number between 1 and 100")
    
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    #数字をランダムに選択する
    random_number= random_select_number()
    #easy or hardのチャンス回数を設定する
    easy_attempt_num = 10
    hard_attempt_num = 5

    if level == "easy":
            make_a_guess(easy_attempt_num,random_number)
    elif level == "hard":
            make_a_guess(hard_attempt_num,random_number)

#正解の数字を一つ選ぶ
def random_select_number():
    random_number = random.randint(1, 100)
    print(f"answer: {random_number}")
    return random_number

#チャンス回数を表示する
#Make a guess:で入力した数字が当たらない場合、チャンス回数が1ずつ減る
#attempt_num:残っているチャンス回数
def print_chance_number(attempt_num):
        print(f"You have {remain_chance} attempts remainging to guess the number.")
        attempt_num -= 1
        return attempt_num

#予想あれる数字を入力する
def make_a_guess(attempt_num,random_number):
    global remain_chance 
    remain_chance = attempt_num
    right_flag = False
    while not right_flag:
        remain_chance = print_chance_number(remain_chance)
        enter_number = int(input("Make a guess: "))
        #入力した数字が正解の数字より低い場合
        if enter_number < random_number:
            print("Too Low")
        #入力した数字が正解の数字より高い場合
        elif enter_number > random_number:
            print("Too high")
        else:
        #入力した数字が正解の数字の場合、
            print(f"You got it! The answer was {random_number}")
            right_flag = True
        #残っているチャンスがない場合、そのまま終了させる
        if remain_chance == 0:
            print("you don't have any chance")
            right_flag = True
    return right_flag