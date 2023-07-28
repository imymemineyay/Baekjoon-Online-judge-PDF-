n = int(input())
previous_fn_2 = 0
previous_fn_1 = 1

if n == 0:
    print(previous_fn_2)

elif n == 1:
    print(previous_fn_1)

else:
    for _ in range(2,n+1): # n>=2
        fn = previous_fn_2 + previous_fn_1
        previous_fn_2 = previous_fn_1
        previous_fn_1 = fn

    print(fn)