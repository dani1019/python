input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
word = input("Type your message:\n")
change_number = input("Type the shift number:\n")
# print("Here's the encoded result")
#"abcdefg....."
# if Type the shift number enter 5
#"a[i+5]b[i+5]c[i+5]"
#change_number만큼 이동했을 때의 알파벳 출력
for letter in word:
    ord_letter = ord(letter) + 5
    print(chr(ord_letter))

# for index, value in enumerate(word):
#     print(f'{value}: {index}番名: {ord(value)}')

