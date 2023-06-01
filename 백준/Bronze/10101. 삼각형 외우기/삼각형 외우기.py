angle = []

def result(tot, a,b,c):
    if tot != 180:
        print('Error')
    else:
        if a == b and a == c:
            print('Equilateral')
        elif a == b or a == c or b == c:
            print('Isosceles')
        else:
            print('Scalene')
       
for _ in range(3):
    angle.append(int(input()))

tot = sum(angle)
a, b, c = angle

result(tot,a,b,c)