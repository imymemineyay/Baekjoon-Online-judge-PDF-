T = int(input())

for i in range(T): # 케이스 개수
    k = int(input()) # 층 수
    n = int(input()) # 호수 
    tot = [resident for resident in range(1, n+1)] # 0층 호수 별 사람 수
    
    for j in range(k): # 층 수 만큼 반복 
        tot = [sum(tot[0:number]) for number in range(1,n+1) ] # 슬라이스하기 위해 필요
    print(tot[-1])