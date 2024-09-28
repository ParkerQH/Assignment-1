# 더하기1
def add(a, b):
    return a + b

# 빼기
def subtract(a, b):
    return a - b

# 곱하기
def Multiplication(a, b):
    return a * b

# 나누기
def division(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다."
    return a / b

# 출력
def print_result(a, b, symbol, res):
    if symbol == '1':
        sym = "+"
    elif symbol == '2':
        sym = "-"
    elif symbol == '3':
        sym = "*"
    else:
        sym = "/"
    return print(f"{a} {sym} {b} = {res}")

# 프로그램 시작
while True:
    # 사용자 입력
    print("연산을 선택하세요:")
    print("1. 덧셈")
    print("2. 뺄셈")
    print("3. 곱하기")
    print("4. 나누기")
    print("0. 종료하기")

    choice = input("선택 : ")

    # 종료 조건
    if choice == '0':
        print("프로그램을 종료합니다.")
        break

    # 유효한 선택인지 확인
    if choice not in ['1', '2', '3', '4']:
        print("잘못된 입력입니다. 0에서 4 사이의 숫자를 선택해주세요.")
        continue

    num1 = float(input("첫 번째 숫자 입력: "))
    num2 = float(input("두 번째 숫자 입력: "))

    # 결과 계산 및 출력
    if choice == '1':
        result = add(num1, num2)

    elif choice == '2':
        result = subtract(num1, num2)

    elif choice == '3':
        result = Multiplication(num1, num2)

    elif choice == '4':
        result = division(num1, num2)

    #결과 출력
    print_result(num1, num2, choice, result)
