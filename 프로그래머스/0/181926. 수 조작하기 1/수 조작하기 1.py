def solution(n, control):
    num_dic = dict({'w':1,'s':-1,'d':10,'a':-10})
    answer = n
    for i in control:
        answer += num_dic[i]
    return answer