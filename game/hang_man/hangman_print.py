import random
import hangman_words
import hangman_art

#一つの単語を表示させるための処理
def print_word():
    #hangman_words[list]から一つの単語を選ぶ
    #return one word[string]
    hangman_word = random.choice(hangman_words.word_list)
    #選ばれた単語 Stringをlistに変換し3つの文字を選ぶ
    #return three characters[list]
    change_letters = random.sample(list(hangman_word),3)
    #one word[string]からrandomで3つのcharacterを選び'_'に変換する
    #変換された結果は、changes_word[list]に入れる
    changes_word = []
    for letter in list(hangman_word):
        for change_letter in change_letters:
            if letter == change_letter:
                letter = '_'
        changes_word.append(letter) 
    #changes_word[list]をstringに変換し画面に表示する
    change_word_str = ' '
    word = change_word_str.join(changes_word)
    return word, hangman_word

def enter_letter(complete_word,incomplete_word,enter_letter):
    be_complete_word = []
    print(type(incomplete_word))
    #画面上で入力した文字が表示された単語の何番目と一致するか確認する
    #complete_wordをリストに変換する
    complete_word_letter = complete_word.split()
    complete_word_length = len(complete_word_letter)- 1
    for index  in range(complete_word_length):
        print(complete_word_letter[index])