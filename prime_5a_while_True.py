""" Nhập số tự nhiên n > 1 và kiểm tra xem số đó là nguyên tố hay không """

import math

def is_prime(n: int) -> bool:                             
    """Kiểm tra n có nguyên tố hay không"""
    for k in range(2,int(math.sqrt(n)) + 1):                     
        if n % k == 0:                       
            return False                     
    return True

def input_number():
    while True:
        n = int(input("n = "))
        if n <= 1:
            print('Số không hợp lệ! Hãy nhập lại!')
        else:
            return n

def print_result(n):
    if is_prime(n):
        print(f"{n} là số nguyên tố.")
    else:                   
        print(f"{n} là hợp số.")        

def main():
    print('Nhập số tự nhiên n > 1')
    n = input_number()
    print_result(n)

if __name__ == "__main__":
    main()