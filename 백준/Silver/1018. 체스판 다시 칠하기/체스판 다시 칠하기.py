N, M = map(int, input().split())

lst = []
results1 = []
results2 = []

for _ in range(N):
    lst.append(input())


for i in range(N-7):
    for j in range(M-7):
        cnt=0
        cnt2 =0
        for ii in range(i,i+8):
            for jj in range(j,j+8):
                if (ii+jj) % 2 == 0:
                    if lst[ii][jj] != 'W' :  
                        cnt += 1
                    if lst[ii][jj] != 'B' :  
                        cnt2 += 1
                else:
                    if lst[ii][jj] != 'B' :  
                        cnt += 1
                    if lst[ii][jj] != 'W' :    
                        cnt2 += 1
        results1.append(cnt)
        results2.append(cnt2)

print(min(min(results1),min(results2)))