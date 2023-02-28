N, M = map(int,input().split())

basket = [n for n in range(1,N+1)]

for _ in range(M):
    i,j,k = map(int,input().split())
    part_of_basket = basket[k-1:j],basket[i-1:k-1]
    basket[i-1:j] = [item for num in part_of_basket for item in num]
print(*basket)