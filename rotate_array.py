# Xoay mảng cho trước đi d vị trí
# (Liên quan mật mã Cesar: xoay xâu cho trước đi d vị trí trong bảng chữ cái)

def rotate_array(arr, d):
    n = len(arr)
    rotated_arr = [0] * n
    for i in range(n):
        rotated_arr[i] = arr[(i + d) % n]
    return rotated_arr

# my = Lê Huy đấy ^^ Hàm này hay hơn hàm sách viết
def my_rotate_array(arr, d):
    return arr[d:] + arr[:d]

arr = [1, 2, 3, 4, 5, 6, 7, 8]
# Number of positions to rotate
d = 3

print("Original Array:", arr)
print("Rotated Array:", rotate_array(arr, d))
print("My Rotated Array:", my_rotate_array(arr, d))