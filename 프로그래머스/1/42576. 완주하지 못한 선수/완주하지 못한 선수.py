def solution(participant, completion):
    answer = ''
    name_num = dict()
    for par in participant:
        name_num[par] = name_num.get(par, 0) + 1

    for name in completion:
        name_num[name] -= 1 

    for name in name_num:
        if name_num[name] == 1:
            answer += name

    return answer