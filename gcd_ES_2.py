"""Tính ước chung lớn nhất và bội chung nhỏ nhất của 2 số tự nhiên"""

def gcd(a, b):
    """Tính ước chung lớn nhất của 2 số tự nhiên (theo thuật toán Euclide)"""
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Tính bội chung nhỏ nhất của 2 số tự nhiên"""
    return (a * b) // gcd(a,b)

a = int(input('Nhập số tự nhiên a = '))
b = int(input('Nhập số tự nhiên b = '))
print(f'Ước chung lớn nhất của {a} và {b} là: {gcd(a,b)}')
print(f'Bội chung nhỏ nhất của {a} và {b} là: {lcm(a,b)}')
