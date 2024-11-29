""" thư ký Bard làm tốt lắm! https://g.co/bard/share/fa4937570535
Để có thể gọi các phương thức sequence(), length(), và max_value()
của class Collatz mà KHÔNG CẦN TẠO ĐỐI TƯỢNG,
bạn có thể sử dụng phương thức staticmethod() của class.
Phương thức staticmethod() sẽ biến một phương thức thành một phương thức tĩnh,
có thể được gọi mà không cần tạo đối tượng của class.
Lưu ý: Nếu không dùng staticmethod() mà dùng method thông thường của class
thì sẽ làm cho mã của bạn trở nên kém linh hoạt hơn.
Ví dụ, nếu bạn muốn tính toán dãy Collatz của một số tự nhiên khác,
bạn cần tạo một đối tượng mới.
"""
def collatz(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1

class Collatz:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def sequence(value):
        """Tính toán dãy Collatz của số tự nhiên value."""
        current_value = value
        sequence = [current_value]
        while current_value > 1:
            current_value = collatz(current_value)
            sequence.append(current_value)
        return sequence

    @staticmethod
    def length(value):
        """Tính toán độ dài của dãy Collatz của số tự nhiên value."""
        current_value = value
        length = 1
        while current_value > 1:
            current_value = collatz(current_value)
            length += 1
        return length

    @staticmethod
    def max_value(value):
        """Tính toán giá trị lớn nhất của dãy Collatz của số tự nhiên value."""
        current_value = value
        max_value = value
        while current_value > 1:
            current_value = collatz(current_value)
            if current_value > max_value:
                max_value = current_value
        return max_value

print(Collatz.sequence(13))
print(Collatz.length(13))
print(Collatz.max_value(13))

print(f'{'n'.center(3)} {'length'.center(5)} {'max value'.center(10)}')

for i in range(100,200):
    print(f'{i:>2d} {Collatz.length(i):>4d} {Collatz.max_value(i):>5d}')
""" lạ không? nhiều 9232 thế nhỉ?
https://math.stackexchange.com/questions/4780807/the-most-famous-trajectory-of-3x1-problem
27  112  9232
31  107  9232
31  107  9232
41  110  9232
47  105  9232
54  113  9232
55  113  9232
62  108  9232
63  108  9232
71  103  9232
73  116  9232
82  111  9232
83  111  9232
91   93  9232
94  106  9232
95  106  9232
96   13    96
97  119  9232
98   26   148
99   26   448
"""