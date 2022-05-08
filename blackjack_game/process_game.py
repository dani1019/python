import random

def select_card():
    start_game = input("Do you  want to play a game of Blackjack? Type 'y' or 'n': ")
    #카드에서 랜덤으로 두개 선택해서 화면에 표시해줌
    my_card = [1,2,3,4,5,6,7,8,9,10,11]
    print(random.sample(my_card, 2))
    #your cards: [9,10]
    #카드에서 하나선택해서 화면에 표시해줌
    #Computer's first card: 8
    #Type 'y' to get another card type 'n' to pass : n
    # →뽑은 두 카드 합이 21에 가깝다 싶으면 n해서 뽑지않는다.
    #Type 'y' to get another card type 'n' to pass : y 
    # →뽑은 두 카드 합이 21에 가깝지 않다 싶으면 n해서 뽑는다.
    #내가 컴퓨터보다 21에 가까우면 You win 반대면 You lose
    #input("Do you  want to play a game of Blackjack? Type 'y' or 'n': ") 반복