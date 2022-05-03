import os

#指値者・指値のデータが保存されるdictionary
bidder_dic={}

#質問が画面に表示され、入力された指値者・指値のデータが保存される
#一番高い指値を提示した指値者の名前と指値が保存される
#highest_bidder_name:一番高い指値を提示した人の名前
#highest_bid: highest_bid
def enter_data():
    print("Welcome to the secret aution program")
    name = input("あなたの名前は何ですか?: ")
    bid_money = input("あなたか出したい指値がいくらですか?: ￥")

    #入力した名前・指値データをbidder_dicに入れる
    bidder_dic[name] = bid_money
    
    #一番高い指値を提示した人の名前
    highest_bidder_name = max(bidder_dic,key=bidder_dic.get)
    
    #一番高い指値
    highest_bid = bidder_dic[highest_bidder_name]
    
    #他の指値者がいるか入力する
    whether_exist_bidder = input("他の指値者はいますか? 'yes' or 'no'を入力してください。")
    
    #他の指値者はありますか?答えに対する処理
    judge_exist_bidder(whether_exist_bidder,highest_bidder_name,highest_bid)

##他の指値者はありますか?答えに対する処理
def judge_exist_bidder(whether_exist_bidder,highest_bidder_name,highest_bid):
    clear = lambda: os.system('cls')
    #yesと入力すると、入力されたデータが画面から消され、次の人の入力画面に切り替わる
    if whether_exist_bidder == "yes":
        clear()
        enter_data()
    #noと入力すると、一番高い指値を提示した人の名前と指値の結果が画面に表示される
    else:
        print(f'指値者は、{highest_bidder_name}で、￥{highest_bid}で指値されました。')