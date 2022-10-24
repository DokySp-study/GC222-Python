s = "we have to learn python "

slist = s.strip().split(" ")
print(f"split 결과 : {slist}")

slist.sort()
print(f"sort 결과 : {slist}")

for i in slist:
    print(i)
