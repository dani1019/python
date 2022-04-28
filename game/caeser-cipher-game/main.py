import process

change_select = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if change_select == "encode":
    process.encode_procees()
else:
    print('exit to not encode')
# for index, value in enumerate(word):
#     print(f'{value}: {index}番名: {ord(value)}')

