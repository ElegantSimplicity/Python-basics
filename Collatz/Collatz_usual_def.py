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

def calculate_all(n):
    current_value = n
    sequence = [current_value]
    max_value = current_value
    length = 1

    while current_value > 1:
        current_value = collatz(current_value)
        sequence.append(current_value)
        length += 1
        max_value = max(max_value, current_value)

    return sequence, length, max_value

sequence, length, max_value = calculate_all(31)
print('Dãy Collatz: ', sequence)
print('Độ dài: ', length)
print('GTLN: ', max_value)
