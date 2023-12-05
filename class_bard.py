# Dùng class, viết chương trình tính chu vi và diện tích
# của hình tròn, hình chữ nhật, và hình tam giác
# Bard gợi ý

class Shape:

    def __init__(self):
        pass

    def tinhChuVi(self):
        raise NotImplementedError("Phương thức tinhChuVi() chưa được định nghĩa")

    def tinhDienTich(self):
        raise NotImplementedError("Phương thức tinhDienTich() chưa được định nghĩa")

##############################
import math

class HinhTron(Shape):

    def __init__(self, r):
        self.r = r

    def tinhChuVi(self):
        return 2 * math.pi * self.r

    def tinhDienTich(self):
        return math.pi * self.r ** 2

##############################
class HinhChuNhat(Shape):

    def __init__(self, l, w):
        super().__init__()
        self.l = l
        self.w = w

    def tinhChuVi(self):
        return 2 * (self.l + self.w)

    def tinhDienTich(self):
        return self.l * self.w

###############################
class HinhTamGiac(Shape):
    
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def tinhChuVi(self):
        return self.a + self.b + self.c

    def tinhDienTich(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

############################
# Tạo hình tròn
htron = HinhTron(5)

# Tính chu vi và diện tích của hình tròn
chuvi = htron.tinhChuVi()
dientich = htron.tinhDienTich()

print("Chu vi của hình tròn là:", chuvi)
print("Diện tích của hình tròn là:", dientich)

# Tạo hình chữ nhật
hcn = HinhChuNhat(10, 5)

# Tính chu vi và diện tích của hình chữ nhật
chuvi = hcn.tinhChuVi()
dientich = hcn.tinhDienTich()

print("Chu vi của hình chữ nhật là:", chuvi)
print("Diện tích của hình chữ nhật là:", dientich)

# Tạo hình tam giác
htam = HinhTamGiac(5, 6, 9)

# Tính chu vi và diện tích của hình tam giác
chuvi = htam.tinhChuVi()
dientich = htam.tinhDienTich()

print("Chu vi của hình tam giác là:", chuvi)
print("Diện tích của hình tam giác là:", dientich)
