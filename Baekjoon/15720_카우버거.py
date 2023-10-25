import sys

# 햄버거, 사이드, 음료수 선택
hamburger, side, beverage = map(int, sys.stdin.readline().split())

hamburger_list = list(map(int, sys.stdin.readline().split()))
hamburger_list.sort()

side_list = list(map(int, sys.stdin.readline().split()))
side_list.sort()

beverage_list = list(map(int, sys.stdin.readline().split()))
beverage_list.sort()

origin_price = 0
sale_price = 0

# 만약 햄버거, 사이드, 음료가 리스트내에 들어있다면 (list 길이가 3이라면) 10% 할인한다
while hamburger_list or side_list or beverage_list :
    price_list = []

    if hamburger_list :
        price_list.append(hamburger_list.pop())

    if side_list :
        price_list.append(side_list.pop())
    
    if beverage_list :
        price_list.append(beverage_list.pop())

    origin_price += sum(price_list)

    if len(price_list) == 3 :       
        sale_price += int(sum(price_list) * 0.9)
    else :
        sale_price += sum(price_list)

print(origin_price)
print(sale_price)

