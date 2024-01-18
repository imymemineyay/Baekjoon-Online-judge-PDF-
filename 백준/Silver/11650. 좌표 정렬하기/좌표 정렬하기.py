import sys
inp = sys.stdin.readline
N = int(inp())

dic = {}
for _ in range(N):
    x, y = map(int,inp().split())
    dic.setdefault(x,[]).append(y)

dic_keys = sorted(dic, key=lambda x : x)

for i in dic_keys:
    for j in sorted(dic[i]):
        print(i,j)