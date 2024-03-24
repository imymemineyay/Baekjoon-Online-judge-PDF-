def solution(sizes):
    answer = 0
    # 가로와 세로를 따로따로 담을 통을 준비한다. 
    length = [] 
    height = []

    # 가로와 세로를 따로따로 담을 때 가로세로를 비교해서 큰 값을 가로에 작은 값을 세로에 담는다.
    for i in sizes:
        if i[0] >= i[1]:
            length.append(i[0])
            height.append(i[1])
        else: 
            length.append(i[1])
            height.append(i[0])
    # 가로의 max값과 세로의 max값을 곱한다. 
    answer = max(length)*max(height)
    return answer