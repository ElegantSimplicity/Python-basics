""" Nhập số tự nhiên n > 1 và kiểm tra xem số đó là nguyên tố hay không """

n = int(input("Nhập số tự nhiên n = "))

def is_prime(n):                         # Định nghĩa hàm is_prime với biến n
    for k in range(2,n):                 #     Cho k chạy từ 2 đến (n-1)
        if n % k == 0:                   #         kiểm tra nếu n chia hết cho k
            return False                 # thì trả về hàm is_prime là False
                                         #     (và tự động thoát hàm, không cần break)
    return True                          # còn nếu kiểm tra hết mà vẫn không chia hết thì trả về hàm is_prime là True
    
if is_prime(n):                          # Nếu is_prime(n) là True (gọi hàm nhớ kèm theo biến) 
    print(f"{n} là số nguyên tố.")       #     thì in ra n là số nguyên tố,
else:                                    # còn nếu không phải thế (is_prime(n) là False)
    print(f"{n} là hợp số.")             #     thì in ra n là hợp số.
