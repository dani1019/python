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
first_result = hangman_print.enter_letter(hang_word,word,enter_letter)
print(f"first_result: {first_result}")

#두 번째 문자를 입력한 후, '_'가 채워진 결과 출력
#print("result: " + result)까지 완성
enter_letter_2 = input("Guess a letter: ")
result = hangman_print.enter_letter(hang_word,first_result,enter_letter_2)
print("result: " + result)