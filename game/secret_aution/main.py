#첫번재 사람이 이름과 낙찰하고 싶은 가격을 입력한다.
#입력한 사람의 이름과 낙찰가격을 key:value로 저장한다.
#다름 입찰자가 있습니까? 라고 했을 때  Yes라고 하면 지금 입력한 사람의 정보가 화면상 지워진다.
#2번쨰 사람이 첫번쨰 사람이 했던 것을 반복한다.
#다름 입찰자가 있습니까? 라고 했을 때  No라고 하면 두번쨰 입력한 사람과 첫번째 입력한 사람의 입찰가를 확인하여,,
#입찰가 높은 사람의 이름과 입찰가격으로 
# 指値者は、${name}で、￥{bid_money}で指値されましたnner is James with a bid of $142'을 프린트 해줌.

print("Welcome to the secret aution program")
name = input("あなたの名前は何ですか?: ")
bid_money = input("あなたか出したい指値がいくらですか?: ")
whether_exist_bidder = input("他の指値者はありますか? 'yes' or 'no'を入力してください。")

#print(f'指値者は、${name}で、￥{bid_money}で指値されましたnner is James with a bid of $142')

bidder_dic={}
bidder_dic[name] = bid_money

print(bidder_dic)

