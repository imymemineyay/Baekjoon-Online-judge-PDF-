def solution(n):
    lst = []
    for i in range(1,11):
        num = 1 
        for j in range(1,i+1):
            num *= j
        lst.append(num)
    
    print(lst)
    
    num = 0
    for i in lst:
        if i <= n:
            num += 1 
        else:
            break
    return num

