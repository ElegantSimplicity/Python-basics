""" Nhập số tự nhiên n > 1 và kiểm tra xem số đó là nguyên tố hay không """

def is_prime(n):                             
    """Kiểm tra n có nguyên tố hay không"""
    for k in range(2,n):                     
        if n % k == 0:                       
            return False                     
    return True

def main():
    n = int(input("Nhập số tự nhiên n = "))
    if is_prime(n):                         
        print(f"{n} là số nguyên tố.")
    else:                             
        print(f"{n} là hợp số.")

if __name__ == "__main__":
    main()
