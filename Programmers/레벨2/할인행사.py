def solution(want, number, discount):
    answer = 0
    want_dict = {}
    test_dict = {}
    
    for w in want :
        test_dict[w] = 0
    
    for i in range(len(number)) :
        want_dict[want[i]] = number[i]
    
    # n째날부터 n+10째날까지 세어서 want에 담긴 물품종류와 number에 담긴 수량이 모두 같으면 
    # 해당 날짜에 회원가입을 한다
    for i in range(len(discount)-9) :
        for key in test_dict.keys() :
            test_dict[key] = 0
       
        sub_arr = discount[i:i+10]
        for j in range(len(sub_arr)) :
            if sub_arr[j] in test_dict :
                test_dict[sub_arr[j]] += 1
        
        if want_dict == test_dict :           
            answer += 1
    
    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
solution(want, number, discount)