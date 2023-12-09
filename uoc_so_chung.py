# Programming style: naive >>> functional >>> OOP
# Bạn sẽ không thể làm việc tốt với bigdata, AI, ... nếu không biết tốt về OOP
# Đề bài: Nhập vào số nguyên dương a và b,
# in toàn bộ ước chung của a và b
a=int(input("Số nguyên dương a = "))
b=int(input("Số nguyên dương b = "))

# Cách 1a: ngây thơ với for
print(f'Các ước số chung của {a} và {b} là:',end = " ")
for k in range(1,min(a,b)+1):
    if a % k == 0 and b % k == 0:
        print(k,end=' ')

# Cách 1b: ngây thơ với while
print(f'\nCác ước số chung của {a} và {b} là:',end = " ")
k = 1
while k < min(a,b):
    if a % k == 0 and b % k == 0:
        print(k,end=' ')
    k +=1    

# Cách 2a: phong cách lập trình hàm (trả về list ước số), dùng for
def USC(a, b):
    tmp = [1]
    for k in range(2,min(a,b)+1):
        if a % k == 0 and b % k == 0:
            tmp.append(k)
    return tmp

# Cách 2b: phong cách lập trình hàm (trả về list ước số), dùng while + tiết kiệm vòng lặp
def uoc_so_chung(a, b):
    tmp = [1]
    k=2
    while k * k < min(a,b):
        if a % k == 0 and b % k == 0:
            tmp.append(k)
        k +=1
    return tmp

# Cách 3: phong cách lập trình hướng đối tượng OOP <<< chuyên nghiệp!
class UocChung:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def in_uoc_chung(self):
        k = 1
        while k * k < min(a,b):
            if a % k == 0 and b % k == 0:
                print(k,end=' ')
            k +=1    

def main():
    print(f'\nCác ước số chung của {a} và {b} là: ', USC(a,b))           # cách 2a
    print(f'\nCác ước số chung của {a} và {b} là: ', uoc_so_chung(a,b))  # cách 2b 

    print(f'Các ước số chung của {a} và {b} là:', end=" ")               # cách 3 (OOP)
    uc = UocChung(a,b)   # uc là một đối tượng của lớp
    uc.in_uoc_chung()

if __name__ == "__main__":
    main()