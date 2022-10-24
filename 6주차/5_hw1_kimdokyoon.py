slist = []

while True:
    item = input("원하는 물건을 입력하세요 : ")
    if item == "quit":
        break
    slist.append(item)
    slist.sort()

    for i, value in enumerate(slist, 1):
        print(i, value)
