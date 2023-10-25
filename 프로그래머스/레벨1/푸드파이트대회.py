def solution(food):
    answer = ''
    food_list = []

    for i in range(1, len(food)):
        for _ in range(food[i] // 2):
            food_list.append(str(i))
    food_reverse = reversed(food_list)

    answer = ''.join(food_list) + '0' + ''.join(food_reverse)
    return answer
