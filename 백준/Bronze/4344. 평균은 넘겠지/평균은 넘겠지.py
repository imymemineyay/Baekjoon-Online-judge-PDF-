C = int(input())

for i in range(C):
  N =  list(map(int,input().split()))
  average = sum(N[1:]) / N[0]
  count = 0
  for k in N[1:]:
    if k > average:
      count += 1
  rate = round(count / N[0] * 100, 3)
  print('{:.3f}%'.format(rate))




