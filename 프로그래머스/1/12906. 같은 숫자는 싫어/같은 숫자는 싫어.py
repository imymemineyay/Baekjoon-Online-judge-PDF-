from collections import deque


def solution(arr):
    answer = []
    arr.append(arr[0]+1)

    arr_dequeue = deque(arr)

    for number in list(arr_dequeue):
        if len(arr_dequeue) <= 1:
            break

        else:
            if number != arr_dequeue[1]:
                num = arr_dequeue.popleft()
                answer.append(num)
            else:
                arr_dequeue.popleft()
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer