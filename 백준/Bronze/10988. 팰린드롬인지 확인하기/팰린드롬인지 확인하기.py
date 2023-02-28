word = input().lower()

if list(word) == list(reversed(word)):
    print(1)
else:
    print(0)