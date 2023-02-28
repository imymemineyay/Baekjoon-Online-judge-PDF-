N = int(input())
num = 2*N-1
for j in range(1,2*N,2):
    star = '*' * j
    center_star1 = star.center(num)
    print(center_star1.rstrip())
for k in range(2*N-3,0,-2):
    star = '*' * k
    center_star2 = star.center(num)
    print(center_star2.rstrip())