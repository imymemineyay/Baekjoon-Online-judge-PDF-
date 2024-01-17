N = input()

lst = [0] * 10


for n in N :
    idx = int(n)
    lst[idx] += 1 

sorted = []
for i in reversed(range(10)):
    if lst[i] != 0:
        for _ in range(lst[i]):
            sorted.append(i)

print(*sorted, sep='')