def solution(num_list):
    answer = []
    zzak = 0
    hol = 0
    
    for i in num_list:
        if i % 2 == 0:
            zzak += 1
        else:
            hol += 1
    answer.extend([zzak, hol])
    return answer