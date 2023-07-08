# 절대값을 사용하여 풀는 법 
n = int(input())

for i in range(1, 2*n):
    col = 2 *n 
    star = (n - abs(n-i))
    l = '*' *star + ' '*(col-2*star)+ "*" * star
    print(l)