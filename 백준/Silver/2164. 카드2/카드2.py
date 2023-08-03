from collections import deque
deque_list = deque()

N = int(input())

deque_list.extend([i for i in range(1, N + 1)])


while len(deque_list) != 1:
    first_num = deque_list.popleft()
    second_num = deque_list.popleft()
    deque_list.append(second_num)
print(*deque_list)

