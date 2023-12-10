# Xoay mảng cho trước đi k vị trí
# (Liên quan mật mã Cesar: xoay xâu cho trước đi k vị trí trong bảng chữ cái)

# Hàm này tốn bộ nhớ
def rotate_arrayA(arr, k):
    n = len(arr)
    rotated_arr = [0] * n
    for i in range(n):
        rotated_arr[i] = arr[(i + k) % n]
    return rotated_arr

# Hàm này gọn nhưng vẫn tốn bộ nhớ
def rotate_arrayB(arr, d):
    return arr[d:] + arr[:d]

# Nhớ luôn vào mảng ban đầu
def rotate_arrayC(arr, k):
    n = len(arr)
    k %= n
    for i in range(k):
        temp = arr[0]
        for j in range(n-1):
            arr[j] = arr[j+1]
        arr[n-1] = temp
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8]
d = 3  # Number of positions to rotate

print("Initial array:", arr)
print("Rotated array:", rotate_arrayA(arr, d))
print("Rotated array:", rotate_arrayB(arr, d))
print("Rotated array:", rotate_arrayC(arr, d))

