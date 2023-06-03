N = int(input())

for i in range(1,N+1): # 분해합을 뛰어넘는 생성자가 없기 때문에 -1 로 감소하면서 구해줌 
    tot = sum((map(int,str(i))))
    num_sum =  tot + i
    if num_sum == N:
        result = i
        break
    if i == N:
        result = 0
print(result)