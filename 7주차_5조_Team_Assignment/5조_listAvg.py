score = []
avg = 0

for i in range(10):
    avg += int(input(f"{i + 1}. 점수를 입력하세요: "))

print(f"평균 : {avg/10}")
