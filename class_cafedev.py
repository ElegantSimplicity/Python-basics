# Dùng class, viết chương trình tính chu vi và diện tích
# của hình tròn, hình chữ nhật, và hình tam giác
# https://cafedev.vn/series-tu-hoc-python-tu-co-ban-toi-nang-cao/
# cafedev.vn gợi ý

# Phần 1. Xây dựng lớp trừu tượng Anstract Base Class (ABC)
# có thể lưu phần 1 thành shape.py
# và trong ba file class con Phần 2 sẽ gọi from shape import*

import abc
class Shape(abc.ABC):
    
    @abc.abstractclassmethod
    def tinh_chu_vi(self):
        pass
    
    @abc.abstractclassmethod
    def tinh_dien_tich(self):
        pass

#########################
# Phần 2. Xây dựng 3 lớp con, kế thừa lớp Shape
# có thể tách ra thành 3 file HinhTron.py HinhChuNhat.py HinhTamGiac.py
import math

class Hinh_Tron(Shape):

    def __init__(self, r):
        self.r = r
        
    def tinh_chu_vi(self):
        return 2*math.pi*self.r
    
    def tinh_dien_tich(self):
        return math.pi*math.pow(self.r,2)

#########################
class Hinh_Tam_Giac(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def tinh_chu_vi(self):
        return self.a + self.b + self.c

    def tinh_dien_tich(self):
        # Su dung cong thuc Heron
        p = (self.a + self.b + self.c)/2
        s = math.sqrt(p*(p - self.a)*(p - self.b)*(p - self.c))
        return s

#########################
class Hinh_Chu_Nhat(Shape):

    def __init__(self, chieudai, chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong

    def tinh_chu_vi(self):
        return (self.chieudai + self.chieurong)*2
    
    def tinh_dien_tich(self):
        return (self.chieudai* self.chieurong)
######################
    
if __name__ == '__main__':
    HChuNhat = Hinh_Chu_Nhat(2,3)
    print("Chieu dai hinh chu nhat: ", HChuNhat.chieudai)
    print("Chieu rong hinh chu nhat: ", HChuNhat.chieurong)
    print("Chu vi hinh chu nhat: ", HChuNhat.tinh_chu_vi())
    print("Dien tich hinh chu nhat: ", HChuNhat.tinh_dien_tich())

    Htron = Hinh_Tron(1)
    print("Ban kinh hinh tron: ", Htron.r)
    print("Chu vi hinh tron: ", Htron.tinh_chu_vi())
    print("Dien tich hinh tron: ", Htron.tinh_dien_tich())

    HTamGiac = Hinh_Tam_Giac(2,3,4) 
    print("Ba canh cua tam giac: ", HTamGiac.a, HTamGiac.b, HTamGiac.c)
    print("Chu vi tam giac: ", HTamGiac.tinh_chu_vi())
    print("Dien tichtam giac: ", HTamGiac.tinh_dien_tich())

