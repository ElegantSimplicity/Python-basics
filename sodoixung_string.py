# Saturday 9 Sep 2023
# Nhập vào số tự nhiên. Hãy lập trình để biết số đó có đối xứng hay không.
# Ví dụ: nhập 2345,   in ra: 2345 không đối xứng
# Ví dụ: nhập 35853,  in ra: 35853 đối xứng
# Ví dụ: nhập 668866, in ra: 668866 đối xứng
# Expected time: ten minutes!
x=int(input('Nhập số tự nhiên: '))
y=str(x)
print(f'{x} là số đối xứng.') if y==y[::-1] else print(f'{x} KHÔNG là số đối xứng.')

""" Chú thích: cách viết trên gọn hơn của
if y==y[::-1]:
    print(f'{x} là số đối xứng.')
else:
    print(f'{x} KHÔNG là số đối xứng.')

"""