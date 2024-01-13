# 참고 : https://dduniverse.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8D%A7%EC%B9%A0%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
def solution(n, m, section):
    cnt = 1
    paint = section[0]
    for i in range(1, len(section)) :
        if section[i] - paint >= m :
            paint = section[i]
            cnt += 1
    
    
    return cnt