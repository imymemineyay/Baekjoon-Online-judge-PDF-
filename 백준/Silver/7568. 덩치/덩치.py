N = int(input())
res = 1 # 자신보다 덩치 큰 사람의 수 초기화
res_lst = [] # 
weights = [] # 몸무게 list에 담기
heights = [] # 키 list에 담기

# 자기보다 덩치가 큰 사람의 수 구하기
for _ in range(N):
    x,y = map(int,input().split()) # 몸무게와 키 입력 받기
    weights.append(x)
    heights.append(y)

for i in range(N) : 
    for k in range(N):
        if i == k :
            continue
        else:
            if (weights[i] < weights[k]) and (heights[i] < heights[k]):
                res += 1 
    res_lst.append(res) # i 사람의 최종 res를 list에 담기
    res = 1 # res 초기화 

print(*res_lst)
