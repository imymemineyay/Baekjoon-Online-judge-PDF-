def solution(i, j, k):
    answer = 0
    lst = [str(k) for k in range(i,j+1)]
    for i in lst:
        if str(k) in i:
            for j in i:
                answer += int(str(k) == j)
    return answer