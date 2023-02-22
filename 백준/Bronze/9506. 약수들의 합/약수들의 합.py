while True :
    n = int(input())
    if n == -1 :
        break
    else:
        remainder = []
        for i in range(1,n):
            if n % i == 0 :
                remainder.append(i)
        if n == sum(remainder):
            print(n, '=', end = ' ')
            print(*remainder, sep = ' + ')
        else:
            print(n, 'is NOT perfect.')
