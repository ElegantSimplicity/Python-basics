""" Nhập số tự nhiên n > 1 và kiểm tra xem số đó là nguyên tố hay không """
# Bard xem prime_5a_while_True.py bảo tạm tạm và 
# Bard gợi ý cho bạn cách dùng try except raise ValueError as
# xem bình luận của Bard https://g.co/bard/share/57bdadf2db1c

import math

def is_prime(n: int) -> bool:
    """Kiểm tra n có nguyên tố hay không"""
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

def input_number():
    while True:
        try:
            n = int(input("n = "))
            if n <= 1:
                raise ValueError("Số không hợp lệ!")
            return n
        except ValueError as e:
            print(e)

def main():
    print("Nhập số tự nhiên n > 1")
    n = input_number()
    if is_prime(n):
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} là hợp số.")

if __name__ == "__main__":
    main()