import art
import compare_list
from random import choice

selected_two_compare_list = []

#ゲームStart!
def start_game():
    print(art.logo)
    print_compare_list()

def print_compare_list():
    select_two_compare()
    print(list(selected_two_compare_list))
    for one in selected_two_compare_list:
        print(one)

def select_two_compare():
    global selected_two_compare_list
    for i in range(2):
        selected_two_compare_list = choice(compare_list.famous_list)

