def solution(today, terms, privacies):
    result = []
    rule_dict = {}
    today_split = today.split(".")
    today_to_days = int(today_split[0]) * 28 * 12 + int(today_split[1]) * 28 + int(today_split[2])
    for t in terms :
        rule_dict[t.split()[0]] = int(t.split()[1]) * 28
    
    idx = 0
    for p in privacies :
        idx += 1
        element_list = p.split()
        date_split = element_list[0].split(".")
        date_to_days = int(date_split[0]) * 28 * 12 + int(date_split[1]) * 28 + int(date_split[2])
        if today_to_days > date_to_days + rule_dict[element_list[1]] - 1 :
            result.append(idx)

    
    return result

today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
solution(today, terms, privacies)