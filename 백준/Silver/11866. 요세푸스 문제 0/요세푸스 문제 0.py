from collections import deque
N, K = map(int,input().split())

deque_list = deque([i for i in range(1,N+1)])

ans_str = ''
ans_str += '<'
#print('<',end='')
while len(deque_list) != 0:
    deque_list.rotate(-K+1)
    pop_num = deque_list.popleft()
    ans_str += str(pop_num) + ', '
    #print(pop_num, ',', end='')
print(ans_str[:-2] + '>')
