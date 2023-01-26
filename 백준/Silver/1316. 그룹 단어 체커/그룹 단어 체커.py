N = int(input())

count = N

for _ in range(N):
    word = input()
    for i in range(0, len(word)-1) :
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            count -= 1
            break
print(count)   