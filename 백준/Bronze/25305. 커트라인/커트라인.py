N, k = map(int, input().split())

x = list(map(int, input().split()))

sorted_x = []

while len(x) > 0:
    max_num = max(x)
    sorted_x.append(max_num)
    x.remove(max_num)

score = sorted_x[k-1]

print(score)
