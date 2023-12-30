# trên taskbar, gõ cmd 
# trên cửa sổ cmd, gõ pip install sympy
# Bây giờ thử nghiệm hàm kiểm tra số nguyên tố của sympy

import sympy

#print(sympy.isprime(18)) 
#print(sympy.isprime(23)) 

#print(sympy.isprime(0))
#print(sympy.isprime(1)) 
#print(sympy.isprime(2))

#print(sympy.isprime(3.8)) 
#print(sympy.isprime(-5))
#x = 'abc'
#print(sympy.isprime(x)) 
#print(sympy.isprime(abc)) 

""" Testing: bây giờ hãy làm cho hàm is_prime() của bạn tốt như hàm isprime() của sympy """
import math     # for isnan()

def is_prime(n):
    """Kiểm tra n có là số nguyên tố hay không"""
    if n <= 1 or n != int(n): return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

print(sympy.isprime(18)) 
print(is_prime(18))

print(sympy.isprime(23)) 
print(is_prime(23))

print(sympy.isprime(0))
print(is_prime(0))

print(sympy.isprime(1)) 
print(is_prime(1))

print(sympy.isprime(2))
print(is_prime(2))

print(sympy.isprime(3.8))  # False 
print(is_prime(3.8))       # True >>> cần cải tiến if n <= 1 or n != int(n): return False

print(sympy.isprime(-5))
print(is_prime(-5))

#x = 'abc'
#print(sympy.isprime(x))
#print(is_prime(x))

#print(sympy.isprime(abc)) 
