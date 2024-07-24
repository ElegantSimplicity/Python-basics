# Cách tiếp cận ngây thơ: tốc độ chậm
import time
n = 200
k = 3
print(f'Phương trình a^{k} + b^{k} = c^{k} + d^{k}')
"""Chọn a = min(a,b,c,d) và b = max(a,b,c,d) thì 1 <= a < c <= d < b < n"""
print('Bắt đầu tìm nghiệm nguyên ...\n')
start_time = time.time()

number_of_solution = 0
for a in range(1,n):
    for b in range(a+1,n):
        for c in range(a+1,b):
            for d in range(c,b):
                if a**k + b**k == c**k + d**k:
                    print(f'{a}^{k} + {b}^{k} = {c}^{k} + {d}^{k} = {a**k+b**k}')
                    number_of_solution += 1
                    
print(f'\n...... xong! Tìm được {number_of_solution} nghiệm.')
print(f'Thời gian chạy: {time.time() - start_time} giây.')