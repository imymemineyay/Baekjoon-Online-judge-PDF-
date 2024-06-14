def solution(num_list, n):
    answer = [[] for _ in range(len(num_list)//n)]
    num = 0
    
    for i in range(0,len(num_list),n):
        for j in range(i,i+n):
            answer[num].append(num_list[j])        
        num += 1
    return answer