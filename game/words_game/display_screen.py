import random
import words_data

#3箇所の文字が表示されない単語が画面に提示され、表示されない文字を入力し、単語に含まれる文字だったら表示される
#すべての文字が表示されるとゲーム終了する
def play_loop():
    #3箇所の文字が表示されない単語が提示される
    print("You guessed a , that's not in the word .You lose  a life")
    display_word, selected_word= print_word()
    print(display_word)

    #表示されない文字を入力し、単語に含まれる文字だったら表示される
    first_letter = input("Guess a letter: ")
    first_complete_word = complete_word_process(display_word,selected_word,first_letter)

    complete_word = check_complete(first_complete_word,selected_word,first_letter)
    
    #すべての文字が表示されるとゲーム終了する
    print(f'{complete_word}\n')
    print(f'おめでとうございます!\n 単語は  {complete_word}でした')

#単語の中で、表示されない文字がある場合、表示されない文字を入力できるようにする
#すべての文字が表示されるまで繰り返す
#return display_word (最終単語の結果)
def check_complete(display_word,selected_word,letter):
    while '_' in display_word:
        print(f'{display_word}\n')
        letter = input("Guess a letter: ")
        display_word = complete_word_process(display_word,selected_word,letter)
    return display_word

#words_data.word_listから一つの単語を選び、3文字が表示されないようにする
#ex) 'strong' → 'st_o__'
# #return word (画面に表示する単語)   selected_word (randomで選ばれた単語)
def print_word():
    selected_word = random.choice(words_data.word_list)
    #表示されない3文字を単語からrandomで選ぶ
    change_letters = random.sample(list(selected_word),3)

    #単語の3文字を'_'に変換し、changes_word[]に入れる
    changes_word = []
    for letter in list(selected_word):
        for change_letter in change_letters:
            if letter == change_letter:
                letter = '_'
        changes_word.append(letter)

    #changes_word[]をstringに変換する
    change_word_str = ' '
    word = change_word_str.join(changes_word)
    return word, selected_word

#return letter_entered_word (入力された文字が反映された単語)
def complete_word_process(incomplete_word,complete_word,enter_letter):
    #入力された文字を小文字に変換する
    enter_letter_lower = enter_letter.lower()
    #randomで選んだ単語を str → list로 변환
    complete_word_list =list(complete_word)
    #画面に表示される単語  str → list로 변환
    incomplete_word_list = list(incomplete_word.replace(" ", ""))

    #入力された文字がrandomで選んだ単語の何番目なのかindex_dictに保存する
    # result = index_dict = {単語の何番目,入力された文字}
    index_dict = {}
    for index, letter in enumerate(complete_word_list):
            if letter == enter_letter_lower:
                index_dict[index] = enter_letter_lower
    
    #入力された文字が単語の文字に存在する際、その文字が表示されるようにする
    for index, letter in enumerate(incomplete_word_list):
        for dic_index, dic_letter in index_dict.items():
            if index == dic_index:
                incomplete_word_list[dic_index] = dic_letter

    letter_entered_word = ''.join(incomplete_word_list)

    return letter_entered_word