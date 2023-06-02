a, b, c = map(int,input().split())
triangle = [a,b,c]

if max(triangle) < (sum(triangle)-max(triangle)) :
    print(sum(triangle))
else:
    result = (sum(triangle)-max(triangle)) + (sum(triangle)-max(triangle)-1)
    print(result)