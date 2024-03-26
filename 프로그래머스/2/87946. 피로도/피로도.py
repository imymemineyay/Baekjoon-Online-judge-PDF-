def solution(k, dungeons):
    # 탐험 가능 던전 횟수를 카운트 해준다. 
    answer = 0
    # 1. 던전을 나타내는 것의 idx값을 추출해서 조합해준다. 
    from itertools import permutations 
    idx_lst = list(permutations(range(len(dungeons)),len(dungeons)))
    cnt_lst = [0]
    # 2. 조합된 순서대로 던전을 탐험한다. 
    for lst in idx_lst:
        fatigue = k
        cnt = 0
        for idx in lst:
            if fatigue >= dungeons[idx][0]:
                fatigue -= dungeons[idx][1]
                cnt += 1
            else:
                break
        if cnt >= max(cnt_lst):
            cnt_lst = [cnt]
            if cnt == len(dungeons):
                break

    answer = cnt_lst[0]
             
    return answer