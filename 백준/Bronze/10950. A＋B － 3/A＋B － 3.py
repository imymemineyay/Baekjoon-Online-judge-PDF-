T = int(input())

results = []
for i in range(T):
  A, B = map(int,input().split())
  results.append(A+B)

for i in results:
  print(i)