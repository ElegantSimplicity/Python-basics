# Chương trình vẫn chạy, nhưng chỉ ra 1 nghiệm (đúng ra có 135 nghiệm)
# Đố bạn lỗi sai ở đâu? 
import time
n = 200
k = 3
print(f'Phương trình a^{k} + b^{k} = c^{k} + d^{k}')
"""Chọn a = min(a,b,c,d) và b = max(a,b,c,d) thì 1 <= a < c <= d < b < n"""
print('Bắt đầu tìm nghiệm nguyên ...\n')
start_time = time.time()

number_of_solution = 0
arr = [0]
for i in range(1,n+1):
    arr.append(pow(i,k))

a, b = 1, n
while a < b:
    temp_sum = arr[a] + arr[b]
    for c in range(a+1,b):
        for d in range(c,b):
            if temp_sum == arr[c] + arr[d]:
                print(f'{a}^{k} + {b}^{k} = {c}^{k} + {d}^{k} = {temp_sum}')
                number_of_solution += 1

    a += 1
    b -= 1

print(f'\n...... xong! Tìm được {number_of_solution} nghiệm.')
print(f'Thời gian chạy: {time.time() - start_time} giây')
