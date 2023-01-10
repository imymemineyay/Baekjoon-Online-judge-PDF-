generator_lst = []
i = 1
while i <= 10000:
    generator = i + (i // 1000) + (i % 1000 // 100) + (i % 1000 % 100 // 10) + (i % 1000 % 100 % 10)
    generator_lst.append(generator)
    i += 1
for k in range(1,10001):
    if k not in generator_lst:
        print(k)      