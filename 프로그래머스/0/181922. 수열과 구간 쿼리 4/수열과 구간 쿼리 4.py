def solution(arr, queries):
    answer = arr.copy()
    
    for s,e,k in queries:
        for idx, i in enumerate(arr):
            if idx >= s and idx <= e and idx % k == 0 :
                answer[idx] += 1
    return answer