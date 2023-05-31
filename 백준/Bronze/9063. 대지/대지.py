N = int(input())

length = []
height = []

for i in range(N):
    l, h = map(int,input().split())
    length.append(l)
    height.append(h)

area = (max(length) - min(length)) * (max(height) - min(height))

print(area)