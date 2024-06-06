def solution(arr, flag):
    answer = []
    for idx, num in enumerate(flag):
        if num == True:
            answer.extend(list(map(int, list(str(arr[idx])*(arr[idx]*2)))))
        else: 
            answer = answer[:len(answer)-arr[idx]]
    return answer