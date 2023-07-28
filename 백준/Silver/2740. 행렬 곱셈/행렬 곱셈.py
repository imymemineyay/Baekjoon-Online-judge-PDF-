# A 행렬(N*M), B행렬(M*K)의 곱을 출력하기

# A행렬과 B행렬 구하기

N, M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

M, K = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(M)]

# 새로운 N*K 사이즈 행렬식 준비 단계 
c = [[0]*K for _ in range(N)]

def dot(a, b):
  # i 번째 요소를 곱하고 더하기
  res=0
  for i in range(M):
    res += a[i]*b[i]
  return res


for i in range(N):  # 행
  for j in range(K): # 열
    # j번째 열만 추출하기
    b_col = [B[idx][j] for idx in range(M)]
    c[i][j] = dot(A[i], b_col)
  print(*c[i])