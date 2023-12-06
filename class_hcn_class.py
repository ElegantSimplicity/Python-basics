# Tính chu vi và diện tích hình chữ nhật
# Cách tạo class Rectangle
# 2 phương thức của class này là phương thức tính chu vi và phương thức tính diện tích

# Chương trình sử dụng class giúp
# - mô tả hình chữ nhật một cách rõ ràng và gọn gàng hơn.
# - dễ dàng tạo ra nhiều đối tượng hình chữ nhật với các thuộc tính khác nhau.
# - dễ dàng mở rộng tính năng của hình chữ nhật.
# >>> tiện hơn sử dụng hàm

class Rectangle:

    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

if __name__ == "__main__":
    # Tạo đối tượng hình chữ nhật
    hinh_chu_nhat = Rectangle(10, 5)

    # Tính chu vi và diện tích hình chữ nhật
    chu_vi = hinh_chu_nhat.tinh_chu_vi()
    dien_tich = hinh_chu_nhat.tinh_dien_tich()

    # In kết quả
    print("Chu vi hình chữ nhật là:", chu_vi)
    print("Diện tích hình chữ nhật là:", dien_tich)
