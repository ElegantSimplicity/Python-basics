# Nhập số nguyên dương n
# in ra số các chữ số chẵn và số các chữ số lẻ
n=int(input('Nhập số nguyên dương n = '))
even_digits = 0
odd_digits = 0
for k in str(n):
    if int(k)%2 == 0: even_digits +=1
    else: odd_digits +=1

print(f'Số {n} có {even_digits} chữ số chẵn và {odd_digits} chữ số lẻ.')    