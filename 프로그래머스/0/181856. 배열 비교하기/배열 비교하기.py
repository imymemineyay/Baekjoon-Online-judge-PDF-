def solution(arr1, arr2):
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    if arr1_len > arr2_len:
        answer = 1
    elif arr1_len < arr2_len:
        answer = -1
    elif arr1_len == arr2_len:
        if sum(arr1) == sum(arr2):
            answer = 0
        elif sum(arr1) > sum(arr2):
            answer = 1
        else:
            answer = -1
    return answer