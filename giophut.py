# Saturday 9 Sep 2023
# Nhập vào số phút. Hãy đổi ra số giờ và số phút lẻ
# Ví dụ: nhập 210 phút, in ra 3 giờ 30 phút
# Expected time: five minutes!
x=int(input('Nhập số phút: '))
sogio=x//60
sophutle=x%60
print(f'{x} phút là: {sogio} giờ {sophutle} phút')