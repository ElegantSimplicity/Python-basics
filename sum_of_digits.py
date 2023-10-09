# Nhập vào số nguyên dương n.
# Tính tổng các chữ số của n
n=int(input("Nhập số nguyên dương n = "))
sum_of_digits=0
while n>0:
    sum_of_digits += n%10
    n //= 10
print("Tổng các chữ số là ", sum_of_digits)
