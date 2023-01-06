A, B = map(int, input().split())
C = int(input())

M = B + C

if M < 60: 
  print(A, M)
elif M >= 60 and A + (M // 60) < 24:
  A = A + (M // 60)
  M %= 60
  print(A, M)
elif M >= 60 and A + (M // 60) >= 24:
  A = (A + (M // 60)) - 24
  M %= 60
  print(A, M) 