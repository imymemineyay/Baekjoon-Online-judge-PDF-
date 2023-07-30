# 1 분에 한 대당 A, 1분에 두 대당 B, 1분에 세 대당 C
A,B,C = map(int, input().split())

# 입력으로 주어지는 시간 1~100 사이 --> 100개 요소가 들어가는 0 리스트 생성
hours = [0 for _ in range(100)]

# 도착과 출발 시간에 해당되는 자릿수에 1을 추가해주기  (동시간에 차 대수 구하기)
for _ in range(3):
  arrive,depart = map(int,input().split())
  # 도착시간은 계산에 포함되면 안되니까 depart-1 
  for i in range(arrive-1, depart-1):
    hours[i] += 1 

# 0 인 원소 제거된 리스트 만들기 
remove_set = {0}
hours = [hour for hour in hours if hour not in remove_set]

# 계산하기
total_price = hours.count(1) * A + hours.count(2) * B * 2 + hours.count(3) * C *3

print(total_price)

