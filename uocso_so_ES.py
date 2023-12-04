# Đếm số ước số của số nguyên dương n nhập từ bàn phím

# dùng for, đơn giản nhưng chưa tối ưu
def divisor_count0(n):
    s = 0
    for i in range(1, n + 1):
        if n % i == 0: s += 1
    return s

# dùng for, đã tối ưu
def divisor_count1(n):
    s = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n == i*i: s += 1
        elif n % i == 0: s += 2
    return s

# dùng for, đã tối ưu và đẹp code
def divisor_count2(n):       
    s = 0
    i = 1
    while i*i <= n:
        if n == i*i: s += 1
        elif n % i == 0: s += 2
        i += 1
    return s

n = int(input("n = "))
print('Số ước số là: ',divisor_count0(n))
print('Số ước số là: ',divisor_count1(n))
print('Số ước số là: ',divisor_count2(n))