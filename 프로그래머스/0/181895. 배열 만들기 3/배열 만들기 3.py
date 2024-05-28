def solution(arr, intervals):   
    answer = []
    for i,j in intervals:
        answer.extend(arr[i:j+1])
    return answer