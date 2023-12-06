# Dùng hàm, viết chương trình tính chu vi và diện tích
# của hình tròn, hình chữ nhật, và hình tam giác
# Rõ ràng dùng hàm khá phiền phức so với dùng class
# Bard gợi ý

import math

def chu_vi_hinh_chu_nhat(chieu_dai, chieu_rong):
    return 2 * (chieu_dai + chieu_rong)

def dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong):
    return chieu_dai * chieu_rong

def chu_vi_hinh_tam_giac(canh_a, canh_b, canh_c):
    return canh_a + canh_b + canh_c

def dien_tich_hinh_tam_giac(canh_a, canh_b, canh_c):
    p = canh_a + canh_b + canh_c
    return math.sqrt(p * (p - canh_a) * (p - canh_b) * (p - canh_c))

def chu_vi_hinh_tron(ban_kinh):
    return 2 * math.pi * ban_kinh

def dien_tich_hinh_tron(ban_kinh):
    return math.pi * ban_kinh ** 2

def main():
    print("Chọn hình cần tính:")
    print("1. Hình chữ nhật")
    print("2. Hình tam giác")
    print("3. Hình tròn")
    chon = int(input())

    if chon == 1:
        chieu_dai = float(input("Nhập chiều dài a = "))
        chieu_rong = float(input("Nhập chiều rộng b = "))
        print("Chu vi hình chữ nhật:", chu_vi_hinh_chu_nhat(chieu_dai, chieu_rong))
        print("Diện tích hình chữ nhật:", dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong))
    elif chon == 2:
        canh_a = float(input("Nhập cạnh a = "))
        canh_b = float(input("Nhập cạnh b = "))
        canh_c = float(input("Nhập cạnh c = "))
        print("Chu vi hình tam giác:", chu_vi_hinh_tam_giac(canh_a, canh_b, canh_c))
        print("Diện tích hình tam giác:", dien_tich_hinh_tam_giac(canh_a, canh_b, canh_c))
    elif chon == 3:
        ban_kinh = float(input("Nhập bán kính r = "))
        print("Chu vi hình tròn:", chu_vi_hinh_tron(ban_kinh))
        print("Diện tích hình tròn:", dien_tich_hinh_tron(ban_kinh))
    else:
        print("Chọn không đúng.")

if __name__ == "__main__":
    main()
