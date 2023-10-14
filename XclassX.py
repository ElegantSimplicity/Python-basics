class ConNguoi:
    # Khai báo và gán các giá trị mặc định cho thuộc tính (attribute)
    HoTen = "" 
    Tuoi = 0
    GioiTinh = ""
    # Khai báo các phương thức (method)
    def an(self):
        print(self.HoTen + ' có thể ăn cá!')
    def noi(self, lang = 'Việt Nam'):
        print(self.HoTen + ' có thể nói tiếng ' + lang)
    def hoc(self, prog_lang):
        print(self.HoTen + ' có thể học ' + prog_lang)        

# Khởi tạo X là đối tượng thuộc lớp ConNguoi
X = ConNguoi()
# Gán các thuộc tính của đối tượng X
X.HoTen = "Liên"
X.Tuoi = 22
X.GioiTinh = "nữ"
print(X.HoTen)
print(X.Tuoi)
print(X.GioiTinh)

# Truy cập các phương thức trong lớp ConNguoi thông qua đối tượng X
X.an()
X.noi()
X.noi("Hàn Quốc")
X.hoc('Python')
