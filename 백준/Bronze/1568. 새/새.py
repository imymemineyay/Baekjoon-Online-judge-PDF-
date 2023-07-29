N = int(input())

# 새들은 1부터 모든 자연수를 오름차순으로 노래 부름
k = 1 
time = 0
# 자연수 오름차순으로 노래 부름
while True : 
# 나무 위에 새가 존재하지 않는다면 멈춤
  if N == 0:
    break
  else:
# 노래 수가 나무 위의 새의 수보다 적을 때 진행
    if k <= N : 
# 노래 수만큼 새는 하늘로 나라감 N = N-k
      N -= k
# k의 수는 누적됨
      k += 1
# N -= k이기 때문에 time이 1씩 증가한
      time += 1
# k>N 일때 k는 다시 1로 초기화됨
    elif k > N :
      k = 1
print(time)