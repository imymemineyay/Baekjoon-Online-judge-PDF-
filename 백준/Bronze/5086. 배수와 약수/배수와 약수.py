while True :
    A, B = map(int,input().split())
    if A == 0 and B == 0 :
        break
    elif A > B and A % B == 0 :
        print('multiple')
    elif A < B and B % A == 0 :
        print('factor')
    elif A % B != 0 or B % A != 0 :
        print('neither')