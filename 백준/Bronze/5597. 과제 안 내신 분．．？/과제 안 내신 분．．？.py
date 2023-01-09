lst = []
for i in range(28):
  a = int(input())
  lst.append(a)

hw = [] 
for i in list(range(1,31)):
  if i not in lst:
    hw.append(i)
print(min(hw))
print(max(hw))