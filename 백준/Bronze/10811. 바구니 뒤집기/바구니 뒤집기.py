N, M = map(int,input().split())

basket = [n for n in range(1,N+1)]

for m in range(M):
    i, j = map(int,input().split())
    part = list(reversed(basket[i-1:j]))
    basket[i-1:j] = part
print(*basket)