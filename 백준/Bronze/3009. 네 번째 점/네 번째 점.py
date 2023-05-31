length = []
height = []
for _ in range(3):
    l, h = map(int,input().split())
    length.append(l)
    height.append(h)


if length.count(max(length)) == 1:
    result_length = max(length)
    idx = length.index(result_length)
    if height[idx] == max(height):
        result_height = height[idx] - (max(height) - min(height))
    else:
        result_height = height[idx] + (max(height) - min(height))

else:
    result_length = min(length)
    idx = length.index(result_length)
    if height[idx] == max(height):
        result_height = height[idx] - (max(height) - min(height))
    else:
        result_height = height[idx] + (max(height) - min(height))

print(result_length,result_height)