N, M = map(int,input().split())

A = []
for i in range(N):
    A.append(list(map(int,input().split())))

B = []
for i in range(N):
    B.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        print(A[i][j]+B[i][j], end=' ')
    print()
