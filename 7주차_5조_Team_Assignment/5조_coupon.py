price = int(input("가격을 입력하세요: "))
coupon = input("쿠폰을 입력하세요(vip/member/etc): ")

if coupon == "vip":
    total = int(price * 0.7)

elif coupon == "member":
    total = int(price * 0.8)

else:
    total = int(price * 0.95)

print("할인된 가격은 ", total)
