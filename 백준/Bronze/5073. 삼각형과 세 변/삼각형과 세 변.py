def result(angles,a,b,c):
    if max(angles) >= sum(angles)-max(angles):
        print('Invalid')
    elif a == b and a == c:
        print('Equilateral')
    elif a ==b or a==c or b==c :
        print('Isosceles')
    else:
        print('Scalene')


while True :
    angle = map(int, input().split())
    angles = list(angle)
    a, b, c = angles
    if angles == [0, 0, 0]:
        break
    else: 
        result(angles,a,b,c)