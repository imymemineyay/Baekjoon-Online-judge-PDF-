# 일곱 난쟁이의 키의 합이 100이 되는 수를 구해야함
# 9명 중 2명의 키의 합을 전체에서 빼줬을 때 100이 되면 됨

nine_midgets = [int(input()) for _ in range(9)]
cond = sum(nine_midgets)

found = False
for i in range(len(nine_midgets)-1):
    for j in range(i+1,len(nine_midgets)):
        tot = 0
        tot = cond - nine_midgets[i] - nine_midgets[j]
        if tot == 100:
            nine_midgets.pop(i)
            nine_midgets.pop(j-1)
            found = True
            break
    if found:
      break


for k in sorted(nine_midgets):
    print(k) 
