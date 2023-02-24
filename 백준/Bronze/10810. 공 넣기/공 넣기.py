N, M = map(int,input().split())

basket = [0 for i in range(N)]

for i in range(M):
    i, j, k = map(int, input().split())
    basket[i-1:j] = [k for j in range(j-i+1)]

print(*basket, sep=' ')