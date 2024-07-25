# Cải tiến 1: tính trước mảng lũy thừa k để không phải tính lại mỗi lần lặp 
# Cải tiến 2: do dãy càng ngày càng thưa, nên ta duyệt cuối mảng trước: theo b, d, c
# Cải tiến 3: ko dùng (temp in arr) vì tốn việc duyệt cả mảng arr. Ta dùng trực tiếp cbrt
#   n    số nghiệm    thời gian chạy (giây)
# 1000     1598           136 
#  500      565            20
#  300      254             5
#  200      135             1.5
#  100       45             0.2
#   50        12            0.05
import numpy as np
import time
n = 20
k = 3
print(f'Phương trình a^{k} + b^{k} = c^{k} + d^{k} với a,b,c,d bé hơn n = {n}')
"""Chọn a = min(a,b,c,d) và b = max(a,b,c,d) thì 1 <= a < c <= d < b < n"""
print('Bắt đầu tìm nghiệm nguyên ...\n')
start_time = time.time()

number_of_solution = 0
arr = [0]
for i in range(1,n+1):
    arr.append(np.power(i,k))

for b in range(n-1,3,-1):
    for d in range(b-1,2,-1):
        for c in range(d-1,1,-1):
            temp = arr[c] + arr[d] - arr[b]
            if temp > 0:
                a = np.cbrt(temp)
                if int(a) == a:
                    print(f'{int(a)}^{k} + {b}^{k} = {c}^{k} + {d}^{k}')
                    number_of_solution += 1

print(f'\n...... xong! Tìm được {number_of_solution} nghiệm nguyên.')
print(f'Thời gian chạy: {time.time() - start_time} giây.')