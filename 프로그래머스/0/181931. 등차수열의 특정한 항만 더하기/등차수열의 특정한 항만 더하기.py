def solution(a, d, included):
    n = d*(len(included)-1)+a
    lst = list(range(a,n+1,d))
    answer = 0
    print(lst)
    for idx, j  in enumerate(included):
        if j == True:
            answer += lst[idx]
    return answer