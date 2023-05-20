areas = [[0 for j in range(100)] for i in range(100)]
counts = 0

origami_cnt = int(input())

for i in range(origami_cnt):
    x,y = list(map(int,input().split()))
    for x_idx in range(x, x+10):
        for y_idx in range(y, y+10):
            areas[x_idx][y_idx] = 1

for area in areas:
    counts += area.count(1)

print(counts)