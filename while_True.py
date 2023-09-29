"""
Bài học: while True ... break chính là cấu trúc Repeat ... until

Đề bài: Nhập vào một dãy số nguyên dương, ngưng nhập khi người dùng nhập -1.
Sau khi nhập xong, in số lớn nhất, số nhỏ nhất trong những số vừa nhập
"""
a=[]
while True:
    n=int(input('Nhập số nguyên dương: '))
    if n!=-1:
        a.append(n)
    else:
        break

print('Dãy đã nhập vào: ',a)
print('Số lớn nhất: ',max(a))
print('Số nhỏ nhất: ',min(a))