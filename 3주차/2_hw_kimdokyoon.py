print("정수를 입력하세요", end=": ")
inp = int(input())
print(
    "자리수의 합은 {}이다".format(
        (inp // 1000) + (inp // 100 % 10) + (inp // 10 % 10) + (inp % 10)
    )
)
