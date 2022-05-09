import random
add_select_card_flag = True
start_game = True
my_cards = []
computer_cards = []
cards = [1,2,3,4,5,6,7,8,9,10,11]

def select_card():
    start_game = input("Do you  want to play a game of Blackjack? Type 'y' or 'n': ")
    #카드에서 랜덤으로 두개 선택해서 화면에 표시해줌
    #自分のカードを2枚選択する
    my_cards = random.sample(cards, 2)
    print(f'my_cards: {my_cards}')
    #コンピューターがカード1枚を選択する
    computer_first_card = random.choice(cards)
    computer_cards.append(computer_first_card)
    print(f'computer_cards: {computer_cards}')

    add_select_card(my_cards,computer_cards)

def add_select_card(my_cards,computer_cards):
    select_y_or_n = input("Type 'y' to get another card type 'n' to pass : n: ")
    if select_y_or_n == "y":
        my_second_card = random.choice(cards)
        print(f'my_second_card: {my_second_card}')
        my_cards.append(my_second_card)
        computer_second_card = random.choice(cards)
        print(f'computer_second_card: {computer_second_card}')
        computer_cards.append(computer_second_card)
    
    for my_card in my_cards:
        print(my_card)
        
    for computer_card in computer_cards:
        print(computer_card)

    # →뽑은 두 카드 합이 21에 가깝다 싶으면 n해서 뽑지않는다.
    #Type 'y' to get another card type 'n' to pass : y 
    # →뽑은 두 카드 합이 21에 가깝지 않다 싶으면 n해서 뽑는다.
    #내가 컴퓨터보다 21에 가까우면 You win 반대면 You lose
    #input("Do you  want to play a game of Blackjack? Type 'y' or 'n': ") 반복