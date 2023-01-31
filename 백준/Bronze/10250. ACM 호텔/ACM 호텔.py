R = int(input())

for i in range(R):
    H, W, N = map(int, input().split())

    if N % H == 0:
        floor = H
        number = N // H
        room_num = floor*100+number
    else:
        floor = N % H
        number = N // H + 1
        room_num = floor*100+number
    print(room_num)