def solution(participant, completion):
    participant_dic = dict()
    for i in participant :
        participant_dic[i] = participant_dic.get(i,0) + 1
        
    for j in completion:
        participant_dic[j] = participant_dic.get(j) - 1

    answer = [name for name,cnt in participant_dic.items() if cnt >= 1][0]
    return answer