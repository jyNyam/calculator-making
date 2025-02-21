# 사칙연산 계산기 만들기

def add(a, b):
    return a + b

def subtrack(a, b):
    return a - b

def multiplt(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다."
    return a / b

def calculator():
    num1 = float(input("첫 번째 숫자를 입력하세요.: "))
    operator = input("연산자를 입력하세요: ")
    num2 = float(input("두 번째 숫자를 입력하세요: "))

    if operator == "+":
        result = add(num1, num2)

    elif operator == "-":
        result = subtrack(num1, num2)
        
    elif operator == "*":
        result = multiplt(num1, num2)

    elif operator == "/":
        result = divide(num1, num2)

    else:
        print("잘못된 연산자입니다.")
        return
    
    print(f"결과: {result}")

calculator()