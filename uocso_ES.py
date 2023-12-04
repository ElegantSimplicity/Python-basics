# Đếm số ước số và in ra các ước số của số nguyên dương n nhập từ bàn phím

# phiên bản đơn giản, kém hiệu quả
def divisors0(n):
    s = {1,n}
    for i in range(2, n + 1):
        if n % i == 0: s.add(i) 
    return s

# phiên bản tốt hơn dùng for
def divisors1(n):
    s = {1,n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: s.add(i); s.add(int(n/i)); 
    return s

# phiên bản tối nhất dùng while
def divisors2(n):       
    s = {1,n}
    i = 2
    while i*i <= n:
        if n % i == 0: s.add(i); s.add(int(n/i));
        i += 1
    return s

n = int(input("n = "))
print(f'Có {len(divisors0(n))} ước số: ',divisors0(n))
print(f'Có {len(divisors1(n))} ước số: ',divisors1(n))
print(f'Có {len(divisors2(n))} ước số: ',divisors2(n))