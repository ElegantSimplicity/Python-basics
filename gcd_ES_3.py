"""Tính ước chung lớn nhất và bội chung nhỏ nhất của 2 số tự nhiên"""
# Tính theo các thư viện math, numpy: có thể tính UCLN và BCNN của nhiều số
# scipy mở rộng numpy, nên ko cần có thêm hàm gcd(a,b) nữa
# numpy và sympy dở hơi, chỉ tính được cho 2 số
# Kết luận: hiện nay dùng thư viện math là OK nhất!
# Bài tập: hãy thực hành trên dấu nhắc console

import math
import numpy as np
import sympy

a, b, c = 16, 56, 28

print(f'UCLN của {a} và {b} là: {math.gcd(a,b)}  {np.gcd(a,b)}  {sympy.gcd(a,b)}')
print(f'BCNN của {a} và {b} là: {math.lcm(a,b)}  {np.lcm(a,b)}  {sympy.lcm(a,b)}')

print(f'UCLN({a},{b},{c}) là:')
print(math.gcd(a,b,c))               # OK!
#print(np.gcd(a,b,c))                # lỗi
print(np.gcd(np.gcd(a,b),c))         # sửa lỗi, nhưng dài
#print(sympy.gcd(a,b,c))             # lỗi
print(sympy.gcd(sympy.gcd(a,b),c))   # sửa lỗi, nhưng dài