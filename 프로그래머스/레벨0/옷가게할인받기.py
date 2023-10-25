def solution(price):
    answer = price
    if price >= 100000 :
        answer = int(price - (price * 0.05))
    if price >= 300000 :
        answer = int(price - (price * 0.1))
    if price >= 500000 :
        answer = int(price - (price * 0.2))
    return answer