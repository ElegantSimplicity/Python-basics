""" https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
Định lý Lagrange: Mọi số tự nhiên đều có thể biểu diễn (duy nhất hoặc không duy nhất)
thành tổng của 4 bình phương (bằng nhau hoặc khác nhau).
"""
def Lagrange_4_squares(N):
    """Danh sách các bộ tứ (a,b,c,d) các số tự nhiên không giảm
    sao cho  a^2 + b^2 + c^2 + d^2 = n
    """
    n = int(N**0.5) + 1
    for a in range(n):
        for b in range(a,n):
            for c in range(b,n):
                for d in range(c,n):
                    if N == a*a + b*b + c*c + d*d:
                        print(f'{N} = {a}^2 + {b}^2 + {c}^2 + {d}^2')

Lagrange_4_squares(3)
Lagrange_4_squares(31)
Lagrange_4_squares(78)
Lagrange_4_squares(310)