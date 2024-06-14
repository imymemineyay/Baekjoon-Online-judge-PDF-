def solution(n):
    answer = []
    for i in range(2,n+1):
        if n % i == 0:
            num = 0 
            for j in range(2,i+1):
                if i % j == 0 :
                    num += 1
                if num >= 2:
                    continue
            if num == 1:
                answer.append(i)
                
    return answer