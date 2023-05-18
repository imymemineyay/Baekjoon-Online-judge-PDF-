lst = []
maximum = 0
column = 0
row = 0

for i in range(9):
  for j in range(1):
    lst.append(map(int,input().split()))
    a = list(lst[i])
    if max(a) > maximum:
      maximum = max(a)
      column = i
      row = a.index(maximum)
print(maximum)
print(column+1, row+1)