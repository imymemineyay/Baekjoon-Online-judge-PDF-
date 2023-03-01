M = int(input())
N = int(input())

prime_numbers = []  


# 소수 찾기
for i in range(M,N+1) : 
    if i > 1 : 
        count = 0                       
        for j in range(2,i):
            if i % j == 0:
                count +=1  
                break                  
        if count == 0 :                 
            prime_numbers.append(i) 

if len(prime_numbers) >= 1 :    
    print(sum(prime_numbers))
    print(min(prime_numbers))
else:
    print(-1)