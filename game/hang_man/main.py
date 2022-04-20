import random
import hangman_words
import hangman_print

print("You guessed a , that's not in the word .You lose  a life")
#一つの単語を表示する(3つの文字は表示されないようにする)
#첫번째 단어제시
word, hang_word= hangman_print.print_word()
print(word)

#첫번째 문자를 입력한 후, '_'가 채워진 결과 출력
enter_letter = input("Guess a letter: ")
first_result= hangman_print.enter_letter(hang_word,word,enter_letter)
print("first_result: " + first_result)

#두 번째 문자를 입력한 후, '_'가 채워진 결과 출력
enter_letter_2 = input("Guess a letter: ")
result = hangman_print.enter_letter(hang_word,first_result,enter_letter_2)
print("result: " + result)

#enter_letter = input("Guess a letter: ")

#while '_' not in result:
    
#print(result)

#1 .word_list에서 단어하나를 뽑아 제시해 줌
#input에 한글자씩 입력하여 맞으면, 제시된 단어가 하나씩 보이도록
#input에 한글자씩 입력해서 틀리면 행맨 팔다리가 늘어나는 것으로

#print(word_list[])를 랜덤으로 하나 불러옴)

#완성된 단어 apple
#제시된 단어 _p__e
# 입력한 문자라면  a라면, ap__e가 출력됨
# 다음에 입력한 문자가 p라면, app_e가 출력됨
#출력된 문자에 '_'가 없어질 때까 무한 반복