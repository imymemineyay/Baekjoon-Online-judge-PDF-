N = int(input())

num = 0

while N >= 0:
    if N % 5 == 0 :
        num += N // 5
        print(num)
        break
    else:
        N -= 3
        num += 1
else:
    print(-1)
