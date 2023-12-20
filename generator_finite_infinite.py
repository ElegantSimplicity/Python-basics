# In ra các số chính phương không quá n   # Print out square numbers less than or equal to n
# Tạo hàm sinh dùng yield                 # Create a generator function using yield
# 2 loại hàm sinh: hữu hạn và vô hạn      # 2 types of generators: finite and infinite
# Bạn hãy sử dụng cho linh hoạt, hợp lý!
# https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/

def SquaresA():
    i = 1
    # An Infinite loop
    while True:
        yield i*i
        i += 1 

def SquaresB(n):
    i = 1
    # An Infinite loop
    while i*i < n:
        yield i*i
        i += 1 

# Driver code to test the generators SquaresA and SquaresB
for num in SquaresA():
    if num > 100:
        break
    print(num, end= ' ')

print()     # xuống dòng

for num in SquaresB(200):
    print(num, end= ' ')

