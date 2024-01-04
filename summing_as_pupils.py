"""
https://www.geeksforgeeks.org/what-is-the-maximum-possible-value-of-an-integer-in-python/
Python 2.7 có kiểu int và long int 
Python 3 chỉ còn 1 kiểu: int. Tính toán số nguyên lớn rất thoải mái với Python 3.
Đó cũng là ưu điểm của Python 3 so với các ngôn ngữ khác như C++
https://youtu.be/76kZGrbSdps?si=ZpV-ZxX72DWqSWTa
"""
def summing_as_pupils(a, b):
    """Tính tổng 2 số nguyên lớn tùy ý.
    Biến comment lưu cách cộng nhẩm như học sinh
    """

    # Convert 2 số nguyên thành chuỗi.
    a_str = str(a)
    b_str = str(b)

    # Thêm các số không vào đầu (nếu cần) để 2 xâu dài bằng nhau
    n = max(len(a_str), len(b_str))
    m = min(len(a_str), len(b_str))
    if len(a_str) > len(b_str):
        b_str = '0' * (n - m) + b_str
    else:
        a_str = '0' * (n - m) + a_str
    
    # dùng biến toàn cục comment, để lưu quá trình học sinh tính toán 
    global comment
    
    # Sử dụng vòng lặp để cộng từng chữ số của 2 chuỗi với nhau.
    carry = 0                 # để nhớ
    result = ""               # để lưu xâu kết quả
    for i in range(n - 1, -1, -1):
        sum_digit = int(a_str[i]) + int(b_str[i]) + carry
        comment = comment + f'{int(a_str[i])} cộng {int(b_str[i])} là {int(a_str[i]) + int(b_str[i])}'
        if carry > 0:
            comment = comment + f', thêm {carry} là {sum_digit}'
        
        result = str(sum_digit % 10) + result
        carry = sum_digit // 10
        if sum_digit >= 10:
            if i == 0:
                comment = comment + f', viết {sum_digit}'
            else:
                comment = comment + f', viết {sum_digit % 10}, nhớ {carry}'
        comment = comment + '\n'
        
    if carry > 0:
        result = str(carry) + result
        
    return int(result)    # Chuyển kết quả về dạng số nguyên.

a = 996138
b =   5678
# Khởi tạo biến toàn cục, lưu quá trình học sinh tính toán
comment = ""
n = max(len(str(a)),len(str(b)))
print(str(a).rjust(n+1))
print('+')
print(str(b).rjust(n+1))
print('-'* (n+2))
print(summing_as_pupils(a, b))      # như print(a+b)
print(comment)