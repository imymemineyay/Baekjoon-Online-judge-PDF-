lst = []
for i in range(9):
  a = int(input())
  lst.append(a)

print(max(lst))
print(lst.index(max(lst))+1)