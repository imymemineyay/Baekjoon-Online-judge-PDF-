N = int(input())

def han(N):
  if N <=  99:
    count = len(range(N))
  elif N <=110:
    count = 99
  elif N >= 111 :
    k = []
    for i in range(111, N+1):
      mean = float(i % 100 // 10)
      if ((i // 100) + (i % 100 % 10)) / 2 == mean :
        k.append(i)
    count = len(range(99)) + len(k)
  print(count)
han(N)