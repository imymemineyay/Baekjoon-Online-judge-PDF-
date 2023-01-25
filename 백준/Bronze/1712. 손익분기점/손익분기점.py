A, B, C = map(int, input().split())


if C > B :
    N = A // (C-B) + 1
    print(N)
else: 
    print(-1)