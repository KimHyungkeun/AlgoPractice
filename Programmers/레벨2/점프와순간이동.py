def solution(n):
    cnt = 0
    # n을 1이 될때까지 계속 2로 나누는 과정 중에, 나머지가 발생하는 횟수를 누적한다
    # 마지막으로 누적된 값에 +1 을 한다
    while n != 1 :
        if n % 2 != 0 :
            cnt += 1
        n //= 2
    
    return cnt + 1