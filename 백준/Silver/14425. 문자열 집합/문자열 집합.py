N, M = map(int,input().split())
S = set()
check_S = []

# 집합 S
for _ in range(N):
    S.add(input())

# 검사가 필요한 문자열
for _ in range(M):
    check_S.append(input())

result = 0
for i in check_S:
  if i in S :
    result += 1 

print(result)