N = int(input())
dic = {}

for _ in range(N):
    age, name = map(str, input().split())
    dic.setdefault(int(age), []).append(name)

sorted_age = sorted(dic)

for i in sorted_age:
    for j in dic[i] :
        print(int(i),j)