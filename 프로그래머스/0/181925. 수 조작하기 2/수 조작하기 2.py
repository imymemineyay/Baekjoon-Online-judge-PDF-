def solution(numLog):
    dic = dict({1:'w',-1:'s',10:'d',-10:'a'})
    answer = ''
    
    n = numLog[0]
    for i in numLog[1:]:
        kii = i - n 
        answer += dic[kii]
        n = i
    
    return answer