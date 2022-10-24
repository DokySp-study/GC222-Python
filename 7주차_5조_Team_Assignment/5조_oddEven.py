odd = 0
even = 0

for i in range(1, 101):
    if i % 2 == 1:
        odd += i
    if i % 2 == 0:
        even += i

print("홀수의 합 :", odd)
print("짝수의 합 :", even)
