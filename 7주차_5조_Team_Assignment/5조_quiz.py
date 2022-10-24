quiz = []
quiz.append("1.중국의 수도를 선택하세요./1)칭따오/2)상하이/3)베이징/3")
quiz.append("2.인도의 수도를 선택하세요. /1)시라즈/2)뉴델리/3)이스파한/2")
quiz.append("태국의 수도를 선택하세요. /1)컨깬/2)방콕/3)핫야이/2")


for q in quiz:
    target = q.split("/")
    answer = target.pop()

    for line in target:
        print(line)

    if answer == input("--> 답을 선택하세요: "):
        print("--> 정답입니다.!\n")
    else:
        print("--> 오답입니다.!\n")
