N = int(input())

lst = [int(input()) for _ in range(N)]


for i in range(N-1):
    min_idx = i
    for j in range(i+1,N):
        if lst[min_idx] > lst[j]:
            min_idx = j
    lst[i], lst[min_idx] = lst[min_idx], lst[i]

for k in lst:
    print(k)