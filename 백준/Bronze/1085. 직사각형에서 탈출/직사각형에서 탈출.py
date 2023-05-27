x, y, w, h = map(int,input().split())

comparing = [x,y,w-x,h-y]

print(min(comparing))