import random
import hangman_words
import hangman_print

print("You guessed a , that's not in the word .You lose  a life")
#一つの単語を表示する(3つの文字は表示されないようにする)
word, hang_word= hangman_print.print_word()
print(word)


#表示されない単語の文字を予想し入力する
enter_letter = input("Guess a letter: ")
hangman_print.enter_word(hang_word,word,enter_letter)


#1 .word_list에서 단어하나를 뽑아 제시해 줌
#input에 한글자씩 입력하여 맞으면, 제시된 단어가 하나씩 보이도록
#input에 한글자씩 입력해서 틀리면 행맨 팔다리가 늘어나는 것으로

#print(word_list[])를 랜덤으로 하나 불러옴)