import random
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def game_start():
    user_cards = []
    computer_cards = []
    #ユーザー、コンピューターそれぞれ2枚のカード選ぶ
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    #ユーザー、コンピューターカードを表示する
    print(f'your card: {user_cards}')
    print(f'computer_card: {computer_cards}')

    #コンピューターカードを追加的に選ぶ
    add_computer_card(computer_cards)
    #ユーザーカードを追加的に選ぶ
    add_user_card(user_cards,computer_cards)

def add_computer_card(computer_cards):
    #コンピューターが選んだカードの合計が17未満の場合、1枚追加する
    while sum(computer_cards) < 17:
        computer_cards.append(deal_card())

def add_user_card(user_cards,computer_cards):
    target_number = 21
    select_y_or_n = input("Type 'y' to get another card type 'n' to pass : n: ")
    #yを押すと, 私にカードが1枚追加、コンピューターにカード1枚追加される    
    if select_y_or_n == "y":
        user_cards.append(deal_card())
        print(f'your card: {user_cards}')
        print(f'computer_card: {computer_cards}')

        add_user_card(user_cards,computer_cards)
    #nを押すと、カードの合計を計算し、私とコンピューター中で、合計が21に近い人が勝利する
    else:
        print(f'your card: {user_cards}')
        print(f'computer_card: {computer_cards}')
        sum_user_cards = sum(user_cards)
        sum_computer_cards = sum(computer_cards)
        sum_user_cards_near_target_num = abs(sum_user_cards - target_number)
        sum_computer_cards_near_target_num = abs(sum_computer_cards - target_number)

        #ユーザー、コンピューターカードの合計が同じである場合、
        if  sum_user_cards == sum_computer_cards:
            print("It's draw")
        #ユーザーカードの合計が21超えたり、ユーザーカードの合計より、コンピューターカードの合計が21に近い場合
        elif 21 < sum_user_cards or sum_user_cards_near_target_num > sum_computer_cards_near_target_num:
            print("You lose")
        #ユーザーカードの合計がコンピューターカードの合計より21に近い場合
        else:
            print("You win")





    # →뽑은 두 카드 합이 21에 가깝다 싶으면 n해서 뽑지않는다.
    #Type 'y' to get another card type 'n' to pass : y 
    # →뽑은 두 카드 합이 21에 가깝지 않다 싶으면 n해서 뽑는다.
    #내가 컴퓨터보다 21에 가까우면 You win 반대면 You lose
    #input("Do you  want to play a game of Blackjack? Type 'y' or 'n': ") 반복