# Nhập số tự nhiên; in ra chữ số cuối cùng
# mà không dùng phép chia
n=int(input('Input an integer n = '))
# Cách 1: dùng phép chia
print('Chữ số cuối cùng là ',n%10)

# Cách 2: chuyển số về chuỗi và lấy chỉ số -1
last_digit=int(str(n)[-1])
print('The last digit is ',last_digit)