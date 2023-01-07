T = int(input())

total = []
for i in range(0,T):
  A, B = map(int, input().split())
  total.append(A+B)
for i in range(1, T+1):
  print("Case #{0}: {1}".format(i, total[i-1]))