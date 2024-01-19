N = int(input())

dic = {}

for _ in range(N):
    x,y = map(int, input().split())
    dic.setdefault(y,[]).append(x)


dic_keys = sorted(dic, key = lambda x : x)

for i in dic_keys:
    for j in sorted(dic[i]) :
        print(j,i)