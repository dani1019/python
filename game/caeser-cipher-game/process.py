#encode処理メソッド
def encode_procees():
    write_word= input("Type your message:\n").lower()
    #入力した単語に数字が含まれているかどうか判定する
    #False → 次の処理に進む
    #True →入っている場合は、処理せずに、「単語に数字は入れないでください」とメッセージが表示されるようにする
    if any(letter.isdigit() for letter in write_word) == False:
        #単語の各文字をどのぐらい移動したいのか入力する
        #単語'abcd'で、「3」入力すると'defg'となる
        change_number = input("Type the shift number:\n")
        changed_word = []
        #各文字が入力した数字ぐらい移動するように処理する
        #単語'abcd'で、「3」入力すると'defg'となる
        #alphabetのみ処理する
        for index, letter in enumerate(write_word):
            char_number = ord(letter)
            # 'a~z'のord(char_number)範囲が 97~122である
            if 96 < char_number and char_number < 123:
                changed_char_number  = ord(letter) + int(change_number)
                changed_letter = chr(changed_char_number)
                changed_word.append(changed_letter)
            else:
                changed_word.append(letter)
        string_word = ''.join(letter for letter in changed_word)
        print(f'string_word:{string_word}')
    #入力した単語に数字が含まれている場合、処理せずに終了させる
    else:
        print("単語に数字は入れないでください")