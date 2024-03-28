def solution(array, commands):
    answer = []
    # commands의 명령안 요소를 하나씩 추출한다.
    for a,b,c in commands:
    #     하나의 요소 안에 있는 명령을 실행한다. 
    #     배열의 i-1부터 n까지 자른 후, 정렬시킨다.
        lst = sorted(array[a-1:b])
    #      정렬된 배열 중 m-1번째 값을 answer에 담는다.
        answer.append(lst[c-1])
    return [(sorted(array[i-1:j])[k-1]) for i,j,k in commands]