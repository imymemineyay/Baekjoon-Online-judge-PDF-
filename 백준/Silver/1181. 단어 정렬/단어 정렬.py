N = int(input())

st = set()

for _ in range(N):
    st.add(input())

lst = list(st)
lst = sorted(lst)
lst = sorted(lst, key = lambda x : len(x))

print(*lst, sep='\n')