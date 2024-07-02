def solution(arr):
    answer = []
    i = 0
    while i < len(arr):
        if answer == []:
            answer.append(arr[i])
            i += 1
        elif len(answer) > 0 and answer[-1] == arr[i]:
            answer = answer[:-1]
            i += 1 
        elif len(answer) >0 and answer[-1] != arr[i]:
            answer.append(arr[i])
            i += 1 
            
    return answer if len(answer) > 0 else [-1]