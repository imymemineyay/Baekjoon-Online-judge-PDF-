N, X = map(int, input().split())

A = map(int, input().split())
lst = list(i for i in A if i < X)

for i in lst:
  print(i, end=' ')