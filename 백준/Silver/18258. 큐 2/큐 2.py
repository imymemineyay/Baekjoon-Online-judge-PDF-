from collections import deque
import sys

N = int(sys.stdin.readline())

deque_list = deque()

for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        deque_list.append(order[1])
    if order[0] == 'pop':
        if len(deque_list) == 0 :
            print(-1)
        else:
            print(deque_list.popleft())
    if order[0] == 'size':
        print(len(deque_list))
    if order[0] == 'empty':
        if len(deque_list) == 0 :
            print(1)
        else:
            print(0)
    if order[0] == 'front':
        if len(deque_list) !=0:
            print(deque_list[0])
        else:
            print(-1)
    if order[0] == 'back':
        if len(deque_list) != 0 :
            print(deque_list[-1])
        else:
            print(-1)
 
