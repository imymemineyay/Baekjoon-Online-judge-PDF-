import sys
input = sys.stdin.readline

#계수정렬 활용
N = int(input())
counting = [0] * 10000

for _ in range(N):
    i = int(input())
    counting[i-1] += 1

for no in range(len(counting)):
    if counting[no] != 0:
        for _ in range(counting[no]):
            print(no+1)
