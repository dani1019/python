operation_result = 0
bool_repeated_calculation = True

def enter_first_number():
    #一つ目の数字を入力する
    first_number = int(input("What's the first number?: "))
    print('''\
    +
    -
    *
    /''')
    #一つ目の数字と計算したい二番目の数字と演算子を入力する
    repeated_calculation(first_number)

#一つ目の数字と計算したい二番目の数字と演算子を入力する
def repeated_calculation(first_number):
    operation = input("Pick an operation: ")
    #二つ目の数字を入力する
    second_number = int(input("What's the second number?: "))

    #一番目・二番目を入力した演算子により計算する
    calculate_process(first_number,operation,second_number)

#一番目・二番目を入力した演算子により計算する
def calculate_process(first_number,operation,second_number):
    #演算子が+の場合、足し算する
    if operation == "+":
        operation_result = first_number + second_number
        print(f'{first_number}  {operation} {second_number} = {operation_result}')
    #演算子が-の場合、引き算する
    elif operation == "-":
        operation_result = first_number - second_number
        print(f'{first_number}  {operation} {second_number} = {operation_result}')
    #演算子が*の場合、掛け算する
    elif operation == "*":
        operation_result = first_number * second_number
        print(f'{first_number}  {operation} {second_number} = {operation_result}')
    #演算子が/の場合、割り算する
    else:
        operation_result = first_number / second_number
        print(f'{first_number}  {operation} {second_number} = {operation_result}')
    
    #引き続き数字を入力し計算するかについて入力する
    type_yn = input(f"Type 'y' to continue calculating with {operation_result} or type 'n' to start a new calculation: ").lower()

    if type_yn == "y":
        bool_repeated_calculation = True
    else:
        bool_repeated_calculation = False

    type_yn_process(bool_repeated_calculation,operation_result)

#引き続き計算するかに対して、'y'を入力すると、引き続き計算が行われ、'n'を入力すると、そのまま処理が完了する
def type_yn_process(bool_repeated_calculation,operation_result):
    if bool_repeated_calculation:
        repeated_calculation(operation_result)
    else:
        print("計算が完了しました。")

    
    
    
