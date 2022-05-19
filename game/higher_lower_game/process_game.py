import art
import compare_list
from random import randint

#ゲームStart!
def start_game():
    print(art.logo)
    print_compare_list()


def print_compare_list():
    #famous_listのindexをランダムに選択できるようにする
    length_compare_list= len(compare_list.famous_list) - 1
    random_index = randint(0,length_compare_list)

    #famous_listの要素をランダムに選択し画面に表示させる
    print(f"compare_A: {compare_list.famous_list[random_index]}")