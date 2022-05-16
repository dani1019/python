import random
#カードをランダムに選択する
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

#ユーザー、コンピューターカードの結果を画面に表示する
def print_cards(user_cards,computer_cards):
    print(f'your card: {user_cards}')
    print(f'computer_card: {computer_cards}')

def game_start():
    user_cards = []
    computer_cards = []
    #ユーザー、コンピューターそれぞれ2枚のカード選ぶ
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #ユーザー、コンピューターカードを表示する
    print_cards(user_cards,computer_cards)
    #ユーザー、コンピューターカードを追加する
    add_cards(user_cards,computer_cards)

#ユーザー、コンピューターカードを追加する
def add_cards(user_cards,computer_cards):
    is_game_over = False
    while not is_game_over:
        #コンピューターが選んだカードの合計が17未満の場合、カードを追加する
        while sum(computer_cards) < 17:
            computer_cards.append(deal_card())

        #ユーザーカードを追加するか質問が表示される     
        select_y_or_n = input("Type 'y' to get another card type 'n' to pass : n: ")
        #yを押すと, 私にカードが1枚追加、コンピューターにカード1枚追加される    
        if select_y_or_n == "y":
            user_cards.append(deal_card())
            print_cards(user_cards,computer_cards)
            #nを押すと、カードの合計を計算し、私とコンピューター中で、合計が21に近い人が勝利する
        else:
            print_cards(user_cards,computer_cards)
            #ユーザーカード、コンピューターカード結果を比較する
            compare_score(user_cards,computer_cards)
            is_game_over = True

#ユーザー、コンピューターカードの合計を比較する
def compare_score(user_cards,computer_cards):
    target_number = 20
    #ユーザーカードの合計
    sum_user_cards = sum(user_cards)
    #コンピューターカードの合計
    sum_computer_cards = sum(computer_cards)
    #ユーザーカードの合計が21からどのぐらい近いか計算する
    sum_user_cards_near_target_num = abs(sum_user_cards - target_number)
    #コンピューターカードの合計が21からどのぐらい近いか計算する
    sum_computer_cards_near_target_num = abs(sum_computer_cards - target_number)
    
    #ユーザー、コンピューターカードの合計が同じである場合、
    if  sum_user_cards > target_number and sum_computer_cards > target_number:
        print("game restart to over 21")
    elif  sum_user_cards == sum_computer_cards:
        print("It's draw")
    #ユーザーカードの合計が21超えたり、ユーザーカードの合計より、コンピューターカードの合計が21に近い場合
    elif target_number < sum_user_cards or sum_user_cards_near_target_num > sum_computer_cards_near_target_num:
        print("You lose")
    #ユーザーカードの合計がコンピューターカードの合計より21に近い場合
    elif target_number > sum_computer_cards:
        print("You win")