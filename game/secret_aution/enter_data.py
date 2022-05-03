import os

#名前・指値データ入力及び保存
def enter_data():
    print("Welcome to the secret aution program")
    name = input("あなたの名前は何ですか?: ")
    bid_money = input("あなたか出したい指値がいくらですか?: ￥")

    #入力した名前・指値データをbidder_dicに入れる
    bidder_dic={}
    bidder_dic[name] = bid_money

    whether_exist_bidder = input("他の指値者はありますか? 'yes' or 'no'を入力してください。")
    
    return whether_exist_bidder

#他の指値者はありますか?質問に対する処理
def judge_exist_bidder(whether_exist_bidder):
    clear = lambda: os.system('cls')
    #yesすると入力したデータが画面から表示されなくなる
    if whether_exist_bidder == "yes":
        clear()