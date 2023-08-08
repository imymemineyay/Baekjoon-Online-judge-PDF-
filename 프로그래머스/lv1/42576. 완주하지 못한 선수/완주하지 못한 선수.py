def solution(participant, completion):
    p_dic = {p: 0 for p in set(participant)}
    
    for p in participant:
        p_dic[p] += 1

    for j in completion:
        p_dic[j] -= 1

    answer = [name for name,cnt in p_dic.items() if cnt >= 1][0]
    return answer