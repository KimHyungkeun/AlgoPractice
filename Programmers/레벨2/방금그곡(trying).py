# 정답참조 : https://roomedia.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B0%A9%EA%B8%88%EA%B7%B8%EA%B3%A1-2018-KAKAO-BLIND-RECRUITMENT
def solution(m, musicinfos):
    answer = ''

    m = m.replace('A#', 'a').replace('C#', 'c').replace('D#', 'd').replace('F#','f').replace('G#','g')
    print(m)

    candidate_list = []
    for ele in musicinfos :
        ele_split = ele.split(",")
        start_time = int(ele_split[0].split(":")[0]) * 60 + int(ele_split[0].split(":")[1])
        end_time = int(ele_split[1].split(":")[0]) * 60 + int(ele_split[1].split(":")[1])
        ele_sound = ele_split[3].replace('A#', 'a').replace('C#', 'c').replace('D#', 'd').replace('F#','f').replace('G#','g')

        sound_length = len(ele_sound)
        play_time = end_time - start_time

        if play_time < sound_length :
            check_sound = ele_sound[:play_time]
        else :
            check_sound = (ele_sound * (play_time // sound_length)) + ele_sound[:play_time]
            check_sound = check_sound[:play_time]
        
        if m in check_sound :
            candidate_list.append((ele_split[2], play_time, start_time))
            break

    if not candidate_list :
        return "(None)"
    
    candidate_list.sort(key = lambda x : x[1], reverse=True)
    answer = candidate_list[0][0]

    return answer

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
# m = "ABC"
# musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# m =  "ABCDEFG"
# musicinfos = ["11:50,12:04,HELLO,CDEFGAB", "12:57,13:11,BYE,CDEFGAB"]
solution(m, musicinfos)
