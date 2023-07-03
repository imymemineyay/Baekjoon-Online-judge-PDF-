N = int(input())

# 두 가지를 다르게 구해줘서 합치기 
# 1 방법 : 앞의 공백 (4,3,2,1,0), 별 개수 (1,3,5,7,9)
for i in range(2*N//2,0,-1):
    blank = i-1 
    star = 2*N-2*i+1
    print(' '*blank,'*'*star,sep='')
# 2 방법 : 앞의 공백 (1,2,3,4), 별 개수 (7,5,3,1)
for k in range(1,2*N//2):
    blank = k
    star = 2*N - (2*k+1) 
    print(' '*blank, '*'*star, sep='')