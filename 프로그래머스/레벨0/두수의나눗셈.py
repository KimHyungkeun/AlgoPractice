def solution(num1, num2):
    # 두 수의 나눗셈에 대한 몫에 대해서 1000을 곱하고, 정수부분만 표현
    answer = int ((num1 / num2) * 1000)
    return answer