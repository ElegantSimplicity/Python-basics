# Saturday 9 Sep 2023
# Nhập vào số tự nhiên. Hãy lập trình để biết số đó có đối xứng hay không.
# Ví dụ: nhập 2345,   in ra: 2345 không đối xứng
# Ví dụ: nhập 35853,  in ra: 35853 đối xứng
# Ví dụ: nhập 668866, in ra: 668866 đối xứng
# Expected time: ten minutes!
x=int(input('Nhập số tự nhiên: '))
digits= [int(x) for x in str(x)] 
# https://niithanoi.edu.vn/20-doan-code-python-ban-nen-thuoc-long.html

print(digits)  # để làm gì biết không?
print(f'{x} là số đối xứng.') if digits==digits[::-1] else print(f'{x} KHÔNG là số đối xứng.')

# Nên viết thành hàm
def is_symmetric_number(n):
    digits = [int(n) for n in str(n)]
    if digits == digits[::-1]: return True
    else: return False

print(f'{x} là số đối xứng.') if is_symmetric_number(x) else print(f'{x} KHÔNG là số đối xứng.')
