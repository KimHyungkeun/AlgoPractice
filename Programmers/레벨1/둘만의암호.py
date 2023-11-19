def solution(s, skip, index):
    result = ''
    skip_list = []

    # 생략 알파벳 확인
    for word in skip :
        skip_list.append(word)
    
    # idx만큼 알파벳을 글자를 바꾸되, skip list에 있는 글자에 대해서는 카운트를 생략
    for w in s :
        idx = 0
        while idx != index :
            if ord(w) + 1 > 122 :
                w = 'a'
            else :
                w = chr(ord(w) + 1)
            if w in skip_list :
                continue
            else :
                idx += 1
        result += w
    
    return result