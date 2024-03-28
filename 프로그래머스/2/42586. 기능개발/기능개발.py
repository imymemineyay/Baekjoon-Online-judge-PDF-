from collections import deque
import math


def solution(progresses, speeds):
    answer = []
    cnt = 1
    # 먼저 각 기능별로 100%까지 구현하기 위해 걸리는 기간을 다음과 같은 공식((100-progress)//(speed))을 활용해 구하고 
    # 이를 통에 담는다. -> for문, index 활용해 계산 
    queue = deque()
    for idx, progress in enumerate(progresses):
        days = ((100-progresses[idx])/(speeds[idx]))
        queue.append(math.ceil(days))


    # 앞서 구한 기간들을 일일이 비교하면 앞수보다 작거나 같은 뒷수가 몇개 있는지 카운트해준다. --> for 문
    previous_day = queue.popleft()

    # 앞서 구한 기간들을 일일이 비교하면서 앞수보다 작거나 같은 뒷수가 몇개 있는지 구해준다.  --> for 문
    for day in list(queue): 
    # 만약 뒷 수가 마지막 위치에 있는 수가 아니라면
    # 앞수가 뒷수보다 작으면 0개를 더해준다. 그리고 다음에 비교될 앞 수는 뒷수가 된다.
        if (previous_day < day) and (len(queue) != 0):
            cnt += 0
            answer.append(cnt)
            cnt = 1
            previous_day = queue.popleft()
            print('if절 previous_day', previous_day)
    #     만약 앞수가 뒷수보다 크기가 크거나 같다면 1개씩 추가해준다. 그리고 앞수가 뒷수보다 작을 때까지 이 행위를 반복한다.  
        elif (previous_day >= day) and (len(queue) != 0):
            cnt += 1
            queue.popleft()
            print('elif절 previous day:',previous_day)
    #     만약 지금까지 구한 갯수들의 합이 전체 길이의 -2개라면 1개를 더해주고 해당 작업을 종료한다.
        if len(queue) == 0:
            cnt += 0
            answer.append(cnt)
    return answer