N,M = map(int,input().split())
card_num = list(map(int,input().split()))

tot = []

for i in range(N-2) :
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            result = card_num[i]+card_num[j]+card_num[k]

            if M >= result:
                tot.append(result)
print(max(tot))