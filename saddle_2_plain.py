a = [[10, 1, 1],
     [4, 3, 2],
     [8, 7, 1]]

saddle_index = []
m, n = len(a), len(a[0])
for i in range(m):
    for j in range(n):
        cond1 = a[i][j] == max(a[i]) == min(a[k][j] for k in range(m))
        cond2 = a[i][j] == min(a[i]) == max(a[k][j] for k in range(m))
        if cond1 or cond2:
            saddle_index.append((i,j))

if saddle_index:
    print('Điểm yên ngựa:')
    for i, j in saddle_index: 
        print(f'a[{i},{j}] = {a[i][j]}')
else:
    print('Chả có điểm yên ngựa nào!')