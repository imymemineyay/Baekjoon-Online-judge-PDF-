mod = []
for i in range(10):
  a = int(input())
  mod.append(a%42)
mod = set(mod)
print(len(mod))