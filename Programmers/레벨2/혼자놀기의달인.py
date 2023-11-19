def solution(cards):
    answer = 0
    card_use = []
    card_group = []
    
    for i in range(len(cards)) :
        tmp = [cards[i]]
        card_use.append(cards[i]) # 한번 사용한 카드를 기억하는 장소
        start = cards[i]-1
        while cards[start] not in card_use : # 카드의 숫자가 n이면, n번째 카드쪽으로 간다. 만약 이미뽑은 카드면 그곳에서 종료
            card_use.append(cards[start])
            tmp.append(cards[start])
            start = cards[start]-1
        
        card_group.append(tmp)
        if len(card_use) == len(cards) :
            break
    
    card_group.sort(key = lambda x : len(x), reverse=True)
    if len(card_group) == 1 : # 만약 1번그룹외에 아무런 그룹이 없으면 0점 처리
        answer = 0
    else :
        answer = len(card_group[0]) * len(card_group[1]) # 카드를 가장 많이 뽑은 경우에 대한 1번 2번그룹에 대해서, 1번그룹카드수 x 2번그룹카드수가 점수
    return answer