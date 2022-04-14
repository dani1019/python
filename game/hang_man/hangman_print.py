import random
import hangman_print
import hangman_words
import hangman_art 

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
    print(word)
    
    


#def print_art()