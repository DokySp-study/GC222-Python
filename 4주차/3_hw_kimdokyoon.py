num1 = int(input("첫번째 정수를 입력하세요:"))
num2 = int(input("두번째 정수를 입력하세요:"))
num3 = int(input("세번째 정수를 입력하세요:"))
max = 0

max = num1
if max < num2:
    max = num2
if max < num3:
    max = num3

print(f"{num1} ,{num2}, {num3} 중 가장 큰 수는 {max}이다.")
