N, M = map(int, input().split())

basket = [k for k in range(1,N+1)]
for o in range(M):
    i, j = map(int, input().split())
    a = basket[i-1] 
    b = basket[j-1]
    basket[j-1] = a 
    basket[i-1] = b

print(*basket, sep=' ')
