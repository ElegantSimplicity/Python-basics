""" Nhập số tự nhiên n > 1 và kiểm tra xem số đó là nguyên tố hay không 
Giải thích: số nguyên tố là số tự nhiên mà chỉ chia hết cho 1 và chính nó
2,3,5,7,11,13,17, ... là số nguyên tố
4,6,8,10,12,14,15,16, ... là hợp số
1 không phải nguyên tố, cũng không phải hợp số
"""
n = int(input("Nhập số tự nhiên n = "))      # Nhập n

is_prime = True                              # Đầu tiên đặt biến is_prime là True (có là số nguyên tố)
for k in range(2,n):                         # Cho k chạy từ 2 đến (n-1)
    if n % k == 0:                           # kiểm tra nếu n chia hết cho k
        is_prime = False                     # thì đặt biến is_prime là False (không là số nguyên tố)
        break                                # và thoát vòng lặp (vì không cần kiểm tra tiếp nữa, phí)
    
if is_prime:                                 # Nếu is_prime là True
    print(f"{n} là số nguyên tố.")           #     thì in ra n là số nguyên tố,
else:                                        # còn nếu không phải thế (is_prime là False)
    print(f"{n} là hợp số.")                 #     thì in ra n là hợp số.