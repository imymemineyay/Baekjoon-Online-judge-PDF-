jinsu = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N, B = map(int,input().split())

result = ''

while N !=0 :
    result += str(jinsu[N%B])
    N = N // B

print(result[::-1])