"""Nếu bạn muốn sử dụng các tính năng của class,
chẳng hạn như kế thừa, đa hình,
thì bạn nên sử dụng phương thức của class.
Nếu bạn chỉ cần viết một hàm đơn giản để tính toán dãy Collatz,
thì bạn có thể sử dụng lập trình hàm thông thường.
"""
def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

class Collatz:
    def __init__(self, value):
        self.value = value

    def calculate_all(self):
        """Tính toán dãy Collatz, độ dài và giá trị lớn nhất trong một lần."""
        current_value = self.value
        sequence = [self.value]
        max_value = self.value
        length = 1

        while current_value > 1:
            current_value = collatz(current_value)
            sequence.append(current_value)
            length += 1
            max_value = max(max_value, current_value)

        return sequence, length, max_value

a = Collatz(13)
sequence, length, max_value = a.calculate_all()
print('Dãy Collatz: ', sequence)
print('Độ dài: ', length)
print('GTLN: ', max_value)
