import sys 

N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    n = int(sys.stdin.readline())
    lst.append(n)

sorted_lst = sorted(lst)

for i in sorted_lst:
    print(i)