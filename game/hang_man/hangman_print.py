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
    hangman_word = 'apple'
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
    #입력받은 enter_letter을 전부 소문자로 만듦
    print("incomplete_word" + incomplete_word)
    enter_letter_lower = enter_letter.lower()
    #제시했던 단어의 형식을 str -> list로 변환
    complete_word_list =list(complete_word)
    incomplete_word_list = list(incomplete_word)
    #complete_word_letter에 enter_letter가 어느 index에 확인할 수 있는 리스트 작성

    #완성된 단어에, 입력받은 문자가 있는지 체크해서, 리스트에 넣는 처리를 만들었다.
    #일치하는 문자에 대해 dict{index,enter_letter} 형태로 list로 저장함
    #{0: 'a', 1: 'a', 2: 'a', 3: 'a', 4: 'a'}
    #버그 입력받은 문자가 완성된 단어가 있으면,  dict{index,enter_letter} 에 들어가게된.
    #완성된 단어 한 글자 한글자씩 for문을 돌려서 일치하는가 확인하고, 
    #일치하는 조건에서만  dict{index,enter_letter} 형태의 리스트에 넣는 것으로
    index_dict = {}
    for index, letter in enumerate(complete_word_list):
            if letter == enter_letter_lower:
                print("a")
                print("enter_letter_lower: " + enter_letter_lower)
                print()
                index_dict[index] = enter_letter_lower
    
    for i,v in index_dict.items():
        print(i,v)
        print()

    #incomplete_word_list 4글자인데, 8자로 출력이 되는 이유는?
    for index,element in incomplete_word_list:
        print(index,element)
        print()
    
    #dic_index하고 incomplete_word_list index가 같다면 incomplete_word_list에 dic_letter을 넣기
    for index, letter in enumerate(incomplete_word_list):
        for dic_index, dic_letter in index_dict.items():
            if index == dic_index:
                incomplete_word_list[dic_index] = dic_letter
            else:
                print(index)
                print()
    
    for index,element in enumerate(incomplete_word_list):
        print(index , element)

                
    #'incomplete_word_letter'
    # for i in range(0,incomplete_word_len):
    #     for index, value in index_dict.items():
    #         incomplete_word_letter[index] = value
    #         print(f'incomplete_word_letter:" + {i} + "番目: " + {incomplete_word_letter[i]}')
    

    # print()
    # for letter in incomplete_word_letter:
    #     print("letter: "+ letter)

    # letter_entered_word = ''.join(incomplete_word_letter)
    # print("letter_entered_word:" + letter_entered_word)
    
    # return letter_entered_word