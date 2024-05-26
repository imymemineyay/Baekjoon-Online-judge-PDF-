def solution(n):
    for i in range(n,n*6+1,n):
        if i % 6 == 0:
            return i // 6 