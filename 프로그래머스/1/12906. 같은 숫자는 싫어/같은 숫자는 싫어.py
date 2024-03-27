def solution(arr):
    answer = []
    arr_length_minus_1 = len(arr)-1
    # - 앞에서부터 arr의 길이 -1한 숫자만큼 뒷수와 비교한다. 
    for i in range(arr_length_minus_1):  
        # 만약 본인과 뒷수가 같지않다면, 본인의 숫자를 answer에 담는다 
        if arr[i] != arr[i+1]:
            answer.append(arr[i])
            # 단, 본인의 수가 마지막 인덱스라면 뒷자리 숫자 역시 answer에 담아준다 
            if (i == arr_length_minus_1):
                answer.append(arr[i+1])
            #  그렇지 않다면 마지막 인덱스의 경우에만 answer값에 담아준다. <br>
        if i == arr_length_minus_1-1:
            answer.append(arr.pop())
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer