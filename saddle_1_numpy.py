import numpy as np

a = np.array([[10, 1, 1],
              [4, 3, 2],
              [8, 7, 1]]) 

saddle_index = []
m, n = a.shape
for i in range(m):
    for j in range(n):
        cond1 = a[i,j] == max(a[i,:]) == min(a[:,j])
        cond2 = a[i,j] == min(a[i,:]) == max(a[:,j])
        if cond1 or cond2:
            saddle_index.append((i,j))

if saddle_index:
    print('Điểm yên ngựa:')
    for i, j in saddle_index: 
        print(f'a[{i},{j}] = {a[i,j]}')
else:
    print('Chả có điểm yên ngựa nào!')