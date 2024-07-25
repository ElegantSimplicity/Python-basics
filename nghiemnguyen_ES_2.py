# Cải tiến 1: tính trước mảng lũy thừa k để không phải tính lại mỗi lần lặp 
# Cải tiến 2: do dãy càng ngày càng thưa, nên ta duyệt cuối mảng trước: theo b, d, c
# >>>> thời gian n=500,300,200: 178,21,5 giây. n=1000 thì tốn chừng 1h chạy  >>> chưa ổn!
import time
n = 300
k = 3
print(f'Phương trình a^{k} + b^{k} = c^{k} + d^{k}')
"""Chọn a = min(a,b,c,d) và b = max(a,b,c,d) thì 1 <= a < c <= d < b < n"""
print('Bắt đầu tìm nghiệm nguyên ...\n')
start_time = time.time()

number_of_solution = 0
arr = [0]
for i in range(1,n+1):
    arr.append(pow(i,k))

for b in range(n-1,0,-1):
    for d in range(b-1,2,-1):
        for c in range(d-1,1,-1):
            temp = arr[c] - arr[b] + arr[d]
            if temp in arr:
                a = arr.index(temp)
                print(f'{a}^{k} + {b}^{k} = {c}^{k} + {d}^{k}')
                number_of_solution += 1

print(f'\n...... xong! Tìm được {number_of_solution} nghiệm.')
print(f'Thời gian chạy: {time.time() - start_time} giây')


