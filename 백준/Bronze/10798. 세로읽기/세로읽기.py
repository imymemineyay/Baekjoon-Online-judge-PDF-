rows = []
column = []
cnt = 0
result = [] 

for i in range(5):
    row = input()
    if len(row) > 15:
        break
    else:
        rows.append(row)
        a = list(rows)
        if cnt < len(row):
            cnt = len(row)

for k in range(cnt):
    for j in range(5):
        if len(rows[j]) < k+1 :
            continue # continue와 break의 차이점은 continue는 다음 루프 수행, pass는 다음 행동 수행
        else:
            output = rows[j][k]
            result.append(output)
print(*result,sep='')