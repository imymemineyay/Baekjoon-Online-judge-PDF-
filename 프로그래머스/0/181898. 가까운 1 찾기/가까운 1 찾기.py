def solution(arr, idx):
    for i,j in enumerate(arr):
        print(i,j)
        if i >= idx and j == 1:
            print(i,j)
            return i
    return -1
        
