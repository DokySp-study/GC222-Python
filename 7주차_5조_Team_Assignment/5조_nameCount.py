name = input("이름을 입력하세요 : ")
count = 0

for i in name:
    count += len(i)

print("이름은 {}자 입니다.".format(count))
