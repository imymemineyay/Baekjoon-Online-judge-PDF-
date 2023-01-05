a, b, c = map(int,input().split())
f = (a+b) % c
s = ((a%c) + (b%c)) % c
t = (a*b) % c
fo = ((a%c) * (b%c))%c

print(f,s,t,fo, sep='\n')