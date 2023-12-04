def gcd(a, b):
    """Thuật toán Euclide trả về ước chung lớn nhất của hai số nguyên."""
    while a != b:
        if a > b: a -= b
        else: b -= a
    return a

def coprime(a, b):
    if gcd(a, b) == 1: return True
    else: return False

m = int(input('Nhập số nguyên m = '))
n = int(input('Nhập số nguyên n = '))

print('Ước chung lớn nhất là ', gcd(m, n))

if coprime(m, n):
    print('Hai số là nguyên tố cùng nhau.')
else:
    print('Hai số KHÔNG là nguyên tố cùng nhau.')
