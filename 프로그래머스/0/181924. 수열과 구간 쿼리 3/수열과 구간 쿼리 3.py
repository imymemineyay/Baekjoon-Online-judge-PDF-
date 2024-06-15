def solution(arr, queries):
    for i,j in queries:
        a = arr[i]
        b = arr[j]
        arr[i] = b
        arr[j] = a
    return arr