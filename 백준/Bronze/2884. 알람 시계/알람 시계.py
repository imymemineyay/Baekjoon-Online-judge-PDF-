H, M = map(int, input().split())

if M < 45 and H == 0:
  H = 23
  print(H, M + 15)
elif M < 45:
  print(H-1, M + 15)
elif M >= 45:
  print(H, M - 45)