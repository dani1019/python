#パスワード生成
import random
#alphabet
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#数字
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#特殊文字
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
#パスワードに入れるalphapet数の入力
nr_letters= int(input("How many letters would you like in your password?\n")) 
#パスワードに入れる数字数の入力
nr_numbers = int(input(f"How many symbols would you like?\n"))
#パスワードに入れる特殊文字の数の入力
nr_symbols = int(input(f"How many numbers would you like?\n"))
character_list = []

#letters_listからnr_letters数のalphapetを取得
letters_list = random.choices(letters,k=nr_letters)
#numbers_listからnr_numbers数の数字を取得
numbers_list = random.choices(numbers,k=nr_numbers)
#symbols_listからnr_symbols数の特殊文字を取得
symbols_list = random.choices(symbols,k=nr_symbols)

#リストを結合する
character_list = letters_list + numbers_list + symbols_list

#character_listの順番をrandomにする
random.shuffle(character_list)

#パスワードを出力する
print(' '.join(character_list))
