# Tính chu vi và diện tích hình chữ nhật
# Cách thông thường: tạo hàm tính chu vi và hàm tính diện tích

def tinh_chu_vi(chieu_dai, chieu_rong):
    return 2 * (chieu_dai + chieu_rong)

def tinh_dien_tich(chieu_dai, chieu_rong):
    return chieu_dai * chieu_rong

if __name__ == "__main__":
    # Nhập chiều dài và chiều rộng hình chữ nhật
    chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
    chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))

    # Tính chu vi và diện tích hình chữ nhật
    chu_vi = tinh_chu_vi(chieu_dai, chieu_rong)
    dien_tich = tinh_dien_tich(chieu_dai, chieu_rong)

    # In kết quả
    print("Chu vi hình chữ nhật là:", chu_vi)
    print("Diện tích hình chữ nhật là:", dien_tich)
