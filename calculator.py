def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        return "지원하지 않는 연산자입니다."

# 사용자 입력
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

operator = input("연산자를 입력하세요: ")

# 결과 출력
result = calculate(num1, num2, operator)
print(f"결과: {result}")