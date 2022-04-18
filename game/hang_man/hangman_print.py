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
    # テスト用 hangman_word = 'apple'
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
    print(complete_word)
    print(type(complete_word))
    print(incomplete_word)
    print(type(incomplete_word))
    print(enter_letter)
    print(type(enter_letter))
    #입력받은 enter_letter을 전부 소문자로 만듦
    enter_letter_lower = enter_letter.lower()
    print(enter_letter_lower)
    #제시했던 단어의 형식을 str -> list로 변환
    complete_word_letter =list(complete_word)
    #enter_letter_lower가 complete_word 있는지 확인
    #return true or false
    if enter_letter_lower in complete_word:
        print("存在する")
        print(complete_word.index(enter_letter_lower))
    else:
        print("存在しない")

    #입력받은 enter_letter가 complete_word 몇 번째에 있는지 확인
    #enter_letter가 복수로 들어가있을 때는 어떻게 해야할까
    #incomplete_word[complete_word 몇 번째] enter_letter를 넣는다.