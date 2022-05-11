import random
sum_computer_cards = 0
start_game = True
my_cards = []
computer_cards = []
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
target_number = 21

def select_card():
    start_game = input("Do you  want to play a game of Blackjack? Type 'y' or 'n': ")
    #カード2枚がランダムに洗濯され、私に与えられる。
    my_cards = random.sample(cards, 2)
    print(f'your_cards: {my_cards}')
    # コンピューターには、ランダムに1枚のカードが与えられる
    computer_first_card = random.choice(cards)
    computer_cards.append(computer_first_card)
    print(f"computer's first card: {computer_cards}")

    #追加的にカードを洗濯するか選ぶ
    add_select_card(my_cards,computer_cards)

#y,n선택하면, 나 컴퓨터가 하나씩의 카드를 더뽑는다.
#만약 컴퓨터의 카드값이 17이하면 강제로 하나 더 뽑게 한다.
#만약 컴퓨터의 카드값이 17이상이면, 내 카드 값에 따라 더 뽑을지 않뽑을지 질문을 더 한다.


def add_select_card(my_cards,computer_cards):
    #컴퓨터 카드 뽑기
    computer_second_card = random.choice(cards)
    computer_cards.append(computer_second_card)

    #컴퓨터 카드 합이 17이하면 하나 더 뽑기
    while sum(computer_cards) < 17:
        print(f'sum_computer_cards2:{sum(computer_cards)}')
        computer_second_card = random.choice(cards)
        computer_cards.append(computer_second_card)
        print(f'sum_computer_cards3: {sum(computer_cards)} ')

    # select_y_or_n = input("Type 'y' to get another card type 'n' to pass : n: ")
    # #yを押すと, 私にカードが1枚追加、コンピューターにカード1枚追加される    
    # if select_y_or_n == "y":
    #     my_second_card = random.choice(cards)
    #     my_cards.append(my_second_card)
    #     print(f'your card: {my_cards}')

    #     computer_second_card = random.choice(cards)
        
    #     print(f'computer_card: {computer_cards}')

    #     sum_computer_cards = sum(computer_cards)

    #     add_select_card(my_cards,computer_cards)
    # #nを押すと、カードの合計を計算し、私とコンピューター中で、合計が21に近い人が勝利する
    # else:
    #     sum_my_cards = sum(my_cards)
        

    #     sum_my_cards_near_target_num = abs(sum_my_cards -target_number)
    #     sum_computer_cards_near_target_num = abs(sum_computer_cards - target_number)

    #     if sum_my_cards_near_target_num < sum_computer_cards_near_target_num:
    #         print("You win")
    #     else:
    #         print("You lose")





    # →뽑은 두 카드 합이 21에 가깝다 싶으면 n해서 뽑지않는다.
    #Type 'y' to get another card type 'n' to pass : y 
    # →뽑은 두 카드 합이 21에 가깝지 않다 싶으면 n해서 뽑는다.
    #내가 컴퓨터보다 21에 가까우면 You win 반대면 You lose
    #input("Do you  want to play a game of Blackjack? Type 'y' or 'n': ") 반복