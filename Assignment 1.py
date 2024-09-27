#더하기
def add(a, b):
    return a + b
#빼기
def subtract(a, b):
    return a - b

#출력
def print_result(a,b,symbol,res):
    if symbol == '1':
        sym = "+"
    else:
        sym = "-"
    return print(f"{a} {sym} {b} = {res}")

# 사용자 입력
print("연산을 선택하세요:")
print("1. 덧셈")
print("2. 뺄셈")
choice = input("선택 : ")
num1 = float(input("첫 번째 숫자 입력: "))
num2 = float(input("두 번째 숫자 입력: "))

#결과 계산 및 출력
if choice == '1':
    result = add(num1, num2)
    print_result(num1,num2,choice,result)

else:
    result = subtract(num1, num2)
    print_result(num1,num2,choice,result)