N = int(input())

for i in reversed(range(0, N)):
  a = ' ' * i
  b = '*' * (N-i)
  print(a + b)