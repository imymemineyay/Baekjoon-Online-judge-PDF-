T = int(input())

total = []
for i in range(1,T+1):
  A, B = map(int, input().split())
  total.append((A,B,A+B))
for i in range(1, T+1):
  print("Case #{0}: {1} + {2} = {3}".format(i,total[i-1][0],total[i-1][1], total[i-1][2]))