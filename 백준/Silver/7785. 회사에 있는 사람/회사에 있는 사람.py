# 해시 쓰자 (문자 찾기에 아주 적합)

n = int(input()) # 출입 기록 수

# 딕셔너리 생성(enter에) 
company_enter = dict()

# 입력을 받기 
for _ in range(n):
    name, enter_leave = input().split()
    # enter 을 입력 받을 경우 key값에 이름 담고, value에 enter값 담기 
    if enter_leave == 'enter':
        company_enter[name] = enter_leave # enter입력 받을 시 집합에 값 추가
    # leave를 받을 경우 dictionary의 키값 삭제
    else:
        company_enter.pop(name)

sorted_name = sorted(company_enter.keys(),reverse=True) # 정렬 

print(*sorted_name, sep='\n')