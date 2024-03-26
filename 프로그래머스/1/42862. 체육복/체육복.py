def solution(n, lost, reserve):
    answer = 0
    pe = [1 for i in range(n)]

    # 2. 리스트에서 lost의 자리에 있는 수는 0해준다. 
    for i in lost:
        pe[i-1] = 0
    # 3. 리스트에서 reserve의 자리에는 1을 더해준다. 
    for i in reserve:
        pe[i-1] += 1

    # 4. 만약 1이 있는 위치의 앞에 0이라면 왼쪽에 있는 사람한테 옷을 빌려준다. 
    #옷을 빌려주면 -1을 해주고 옷 빌린사람은 +1을 받는다.    
    for idx, num in enumerate(pe):

        if num == 0 and idx!=0 and pe[idx-1]>=2:
                pe[idx] += 1
                pe[idx-1] -= 1

    # 5. 만약 뒤에 2가 있다면 뒷사람한테 옷을 빌려준다.
        elif num == 0 and idx!=(n-1) and pe[idx+1] >= 2:
                pe[idx] += 1
                pe[idx+1] -= 1

    # 6. 만약 pe에 2이상이면 1로 바꿔준다. 
    for idx, i in enumerate(pe):
        if i >= 2:
            pe[idx] = 1

    # 7. 이후 해당 리스트의 값을 더해준다. 
    answer = sum(pe)
    return answer