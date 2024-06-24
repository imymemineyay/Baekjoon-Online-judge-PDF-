def solution(arr):
    answer = []
    if 2 in arr:
        n = arr.index(2)
        n_max = arr[::-1].index(2)
        n_max = len(arr) - n_max
        answer.extend(arr[n:n_max])
    else : 
        answer.append(-1)
    return answer