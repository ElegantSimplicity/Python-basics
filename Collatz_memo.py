""" calculating the chain-length of Collatz chain  
Sử dụng từ điển d để lưu trữ các số đã tính và số bước tương ứng
giúp tăng tốc độ tính toán và tránh lặp lại.
Sử dụng ngăn xếp stack để lưu trữ các số chưa có số bước,
giúp truy ngược chuỗi Collatz và tính toán số bước cho các số đó.
https://codereview.stackexchange.com/a/24198/237307
"""
def collatz_length(n, d={1:1}):
    """Iterative Collatz with memoization
    """
    if n not in d:
        d[n] = collatz_length(3 * n + 1 if n & 1 else n/2) + 1
    return d[n]

def collatz_length_improved(n, d = {1: 1}):
    """Iterative Collatz with memoization
    it's longer code, slower but more robust
    """
    stack = []
    while n not in d:
        stack.append(n)
        n = 3 * n + 1 if n & 1 else n // 2
    c = d[n]
    while stack:
        c += 1
        d[stack.pop()] = c
    return c

#print(collatz_length(2**100))            # >>> error
#print(collatz_length_improved(2**100))    # just fine
from timeit import timeit
print(timeit(lambda:map(collatz_length, range(1, 10**6)), number=10))
print(timeit(lambda:map(collatz_length_improved, range(1, 10**6)), number=10))
