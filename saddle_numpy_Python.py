"""Viết chương trình Python thực hiện những yêu cầu sau:
1. Tạo ma trận vuông bậc n (n nhập từ bàn phím) với các
phần tử là các trị ngẫu nhiên trong đoạn [-10, 10],
xuất ma trận.
2. Tìm các điểm yên ngựa của ma trận trên.

Phần tử Aij gọi là điểm yên ngựa (saddle point) của ma trận A nếu nó vừa
là phần tử nhỏ nhất của dòng i, đồng thời là phần tử lớn nhất của cột j;
hoặc ngược lại, vừa là phần tử lớn nhất của dòng i, đồng thời là phần tử
nhỏ nhất của cột j.
Một ma trận có thể không có hoặc có nhiều điểm yên ngựa.

Benefits of using NumPy:
1. Conciseness: The code is shorter and more readable using NumPy functions.
2. Efficiency: NumPy functions are optimized for performance compared to explicit loops.
3. Scalability: This code can easily be adapted to larger matrices without modification.
"""
import numpy as np
# Already there is random in numpy, do not need to import random

def find_saddle(matrix):
    """Tìm chỉ số (i, j) = (hàng, cột) các điểm yên ngựa của ma trận"""
    row_minima = np.min(matrix, axis=1)
    col_maxima = np.max(matrix, axis=0)
    # https://numpy.org/doc/stable/reference/generated/numpy.where.html
    saddle_index = np.where((matrix == row_minima[:, None]) & (matrix == col_maxima))
    return tuple(zip(*saddle_index))

def main():
    m = int(input("Nhập số hàng ma trận m = "))
    n = int(input("Nhập số cột ma trận n = "))
    matrix = np.random.randint(-10, 11, size=(m, n))
    #matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    """
    # for testing 
    matrix = [[1,2,-3],
              [4,5,4],
              [-3,7,0]]     # 2,4,6 là điểm yên ngựa 
    """
    print(matrix)     # >>> in khá đẹp: căn bên phải
    
    # Tìm các điểm yên ngựa
    saddle_index = find_saddle(matrix)
 
    # Xuất các điểm yên ngựa
    if saddle_index:                   # nếu có (mảng khác rỗng)
        print("Các điểm yên ngựa:")
        for index in saddle_index:
            i, j = index
            print(f"a[{i}][{j}] = {matrix[i][j]:>3d}")

    else:
        print("Ma trận không có điểm yên ngựa.")

if __name__ == '__main__':
    main()