N = int(input())

# 리스트 안에 수 넣기
num_list = [int(input()) for _ in range(N)]
sorted_list = [0 for _ in range(N)]

# 삽입 정렬
# 카드 하나를 뽑고 왼쪽으로 옮기기 

for i in range(N):
  for k in range(N):
    if num_list[i] > num_list[k]:
        a = num_list[i]
        b = num_list[k]
        num_list[k] = a
        num_list[i] = b

for i in reversed(num_list):
    print(i)
