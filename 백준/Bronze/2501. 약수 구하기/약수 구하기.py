N, K = map(int, input().split())

remainder = []
for i in range(1, N+1):
    if N % i == 0 :
        remainder.append(i)
if len(remainder) < K:
    print(0)
else:
    print(remainder[K-1])