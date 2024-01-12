""" ES Python Project: game ĐOÁN SỐ = Guessing number game
Số lần đoán tối đa là:
m = int(math.log(n, 2)) + 1           >>> Đúng!
m = round(math.log(n, 2)) + 1         >>> Sai! (có thể thừa 1 lần đoán)
Tổng quát: m = int(math.log(upper - lower + 1, 2))
Chú ý phân biệt int() và round(). Hỏi Bard!
Đây là ví dụ tốt về gỡ lỗi (debug).
Bài toán toán học: Chỉ ra rằng cần tối đa m = int(math.log(n, 2)) + 1
lượt đoán để đoán ra số tự nhiên bất kỳ được chọn trước trong [1,n] 
"""

import random
import math

def doan_so(n):
    """Bạn đoán số máy tính đã chọn ngẫu nhiên từ 1 tới n"""
    so_dau, so_cuoi = 1, n
    so_ngau_nhien = random.randint(so_dau, so_cuoi)
    m = round(math.log(so_cuoi - so_dau + 1, 2)) + 1

    print("Chào mừng bạn đến với trò chơi 'Đoán số'")
    print(f'Tôi đã chọn một số từ 1 đến {n}.')
    print(f'Bạn có tối đa {m} lần đoán.')
    so_lan_doan = 0
    flag = False
    while so_lan_doan < m:
        du_doan = int(input("Đoán số của bạn: "))
        so_lan_doan += 1
        if du_doan == so_ngau_nhien:
            print(f"Chúc mừng! Bạn đã đoán đúng số {so_ngau_nhien} sau {so_lan_doan} lần.")
            flag = True
            break
        elif du_doan < so_ngau_nhien:
            print(f"Số cần tìm lớn hơn. Hãy đoán tiếp (còn {m-so_lan_doan} lần).")
        else:
            print(f"Số cần tìm nhỏ hơn. Hãy đoán tiếp (còn {m-so_lan_doan} lần).")
        
    if flag == False:
        print(f'Bạn đã không đoán được. Số đó là {so_ngau_nhien}.')
        print('Hãy thay đổi chiến lược đoán.')
     
def chien_luoc_doan_so(n):
    """Chiến lược hiệu quả để chắc chắn đoán ra: BISECTION = CHIA ĐÔI"""
    so_dau, so_cuoi = 1, n
    so_ngau_nhien = random.randint(so_dau, so_cuoi)
    m = int(math.log(so_cuoi - so_dau + 1, 2)) + 1
    
    print("Chào mừng bạn đến với trò chơi 'Đoán số'")
    print(f'Tôi đã chọn một số từ 1 đến {n}.')
    print(f'Chiến lược để bạn đoán ra sau tối đa {m} lần đoán như sau:')
    so_lan_doan = 0
    while so_lan_doan < m:
        du_doan = so_dau + (so_cuoi - so_dau) // 2
        print("Bạn nên đoán: ", du_doan)
        so_lan_doan += 1
        
        if du_doan == so_ngau_nhien:
            print(f"Chúc mừng! Bạn đã đoán đúng số {so_ngau_nhien} sau {so_lan_doan} lượt.")
            break
        elif du_doan < so_ngau_nhien:
            print(f"Số cần tìm lớn hơn. Hãy đoán tiếp (còn {m-so_lan_doan} lượt).")
            so_dau = du_doan + 1
        else:
            print(f"Số cần tìm nhỏ hơn. Hãy đoán tiếp (còn {m-so_lan_doan} lượt).")
            so_cuoi = du_doan - 1
    
if __name__ == "__main__":
    #doan_so(9)
    chien_luoc_doan_so(1_000_000)    # cần tối đa 20 lần đoán
    #chien_luoc_doan_so(8)
    #chien_luoc_doan_so(12)
    
    
    # so sánh int() và round()
    #for i in range(8,20):
     #   mint = int(math.log(i,2))
      #  mround = round(math.log(i,2))
       # print(i,mint,mround)