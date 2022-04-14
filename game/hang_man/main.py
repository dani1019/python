import random
import hangman_words
import hangman_print

print("You guessed a , that's not in the word .You lose  a life")
hangman_print.print_word()

input("Guess a letter: ")
#1 .word_list에서 단어하나를 뽑아 제시해 줌
#이때 화면 중에는 두 글자정도 랜덤으로 _로 가려서 보여줌
#input에 한글자씩 입력하여 맞으면, 제시된 단어가 하나씩 보이도록
#input에 한글자씩 입력해서 틀리면 행맨 팔다리가 늘어나는 것으로

#print(word_list[])를 랜덤으로 하나 불러옴)