""" Nhập số tự nhiên n > 1 và kiểm tra xem số đó là nguyên tố hay không """
# Có thể cải tiến chương trình: nếu n <= 1 thì nhập lại
# Có nhiều cách cải tiến hàm is_prime. Hãy hỏi AI (Bard, Bing, ChatGPT, ...)
# xem thuật toán tốt nhất hiện nay để kiểm tra số nguyên tố là gì
# Đây là 1 cải tiến nhỏ: vòng lặp for chỉ cần chạy từ 2 đến int(math.sqrt(n)) + 1
# math.sqrt(n) là căn bậc hai của n, để dùng cần import math
# Nếu không import math, thì có thể dùng int(n**0.5) + 1

def is_prime(n):                             
    """Kiểm tra n có nguyên tố hay không"""
    for k in range(2,int(n**0.5) + 1):                     
        if n % k == 0: return False                     
    return True

def main():
    n = int(input("Nhập số tự nhiên n = "))
    if is_prime(n): print(f"{n} là số nguyên tố.")
    else: print(f"{n} là hợp số.")

if __name__ == "__main__":
    main()