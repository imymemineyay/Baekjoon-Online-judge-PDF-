A, B, V = map(int, input().split())

remainder = (V-A) % (A-B) 
full_day = (V-A) / (A-B) 

if remainder == 0 :
    Day = int(full_day) + 1
else:
    Day = int(full_day) + 2
print(Day)

# 달팽이는 하루동안 A만큼 오르고 B만큼 내린다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)
# 달팽이가 정상 V 높이까지 오르고 난 후엔 내려가지 않는다
# V <= (A-B) * full_day + A 
# (V-A) / (A-B) <= full_day
# full_day 는 정수이다
# (V-A) / (A-B) 의 나머지가 없을 경우 full_day는 (V-A) / (A-B) 자체다
# (V-A) / (A-B)의 나머지가 있을 경우 full_day는 (V-A) / (A-B)의 몫 + 1 의 값이다.
# V <= (A-B) * full_day + A 에서 A의 하루를 추가해줘야 하기 때문에 
# 나머지 유무에 상관없이 모든 Day엔 1을 더해줘야 한다. 