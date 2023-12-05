# Dùng class, viết chương trình tính chu vi và diện tích
# của hình tròn, hình chữ nhật, và hình tam giác
# Bing gợi ý

import math

class Shape:
    def chu_vi(self):
        pass

    def dien_tich(self):
        pass

class HinhTron(Shape):
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh

    def chu_vi(self):
        return 2 * math.pi * self.ban_kinh

    def dien_tich(self):
        return math.pi * (self.ban_kinh ** 2)

class HinhChuNhat(Shape):
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong

class HinhTamGiac(Shape):
    def __init__(self, canh_a, canh_b, canh_c):
        self.canh_a = canh_a
        self.canh_b = canh_b
        self.canh_c = canh_c

    def chu_vi(self):
        return self.canh_a + self.canh_b + self.canh_c

    def dien_tich(self):
        p = self.chu_vi() / 2
        return math.sqrt(p * (p - self.canh_a) * (p - self.canh_b) * (p - self.canh_c))

# Tạo một hình tròn với bán kính là 5
tron = HinhTron(5)
print("Chu vi hình tròn: ", tron.chu_vi())
print("Diện tích hình tròn: ", tron.dien_tich())

# Tạo một hình chữ nhật với chiều dài là 7 và chiều rộng là 4
cn = HinhChuNhat(7, 4)
print("Chu vi hình chữ nhật: ", cn.chu_vi())
print("Diện tích hình chữ nhật: ", cn.dien_tich())

# Tạo một hình tam giác với các cạnh là 3, 4, 5
tg = HinhTamGiac(3, 4, 5)
print("Chu vi hình tam giác: ", tg.chu_vi())
print("Diện tích hình tam giác: ", tg.dien_tich())
