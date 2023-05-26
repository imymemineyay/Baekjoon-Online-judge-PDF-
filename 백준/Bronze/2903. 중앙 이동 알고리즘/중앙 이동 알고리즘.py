N = int(input())

previous_number = 2

for i in range(0,N):
  previous_number = (previous_number + 2 ** i)

print(previous_number**2)


#  1 2 4 8 16    → 이전 한 변의 개수에 2의 n제곱만큼 더해진다는 규칙 발견 
# 2,3,5,9,17,33  → 한 변의 동그라미 개수 
# 4,9,25,81,...  → 한 변의 동그라미 개수의 제곱이 전체 동그라미 개수라는 규칙 발견