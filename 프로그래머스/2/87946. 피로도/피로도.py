from itertools import *



def solution(k, dungeons):
    # 탐험 가능 던전 횟수를 카운트 해준다. 
    answer = 0
    
    idx_lst = list(permutations(range(len(dungeons))))

    comparing_num = 0
    for dungeon in idx_lst:
        fatigue = k
        cnt = 0
        for idx in dungeon:
            if fatigue >= dungeons[idx][0]: 
                fatigue -= dungeons[idx][1] 
                cnt += 1 

            else:
                break

        comparing_num = max(comparing_num, cnt)
        answer = comparing_num

        if answer == len(dungeons):
            break
             
    return answer