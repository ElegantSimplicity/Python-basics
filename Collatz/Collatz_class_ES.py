""" class Collatz đặc biệt ở chỗ nó chỉ có một phương thức duy nhất,
đó là phương thức khởi tạo __init__.
Các phương thức khác của một lớp thường được sử dụng để thực hiện
các hành động cụ thể liên quan đến các thuộc tính của lớp đó.
Tuy nhiên, trong trường hợp của lớp Collatz,
các thuộc tính chain, length, và max_value chỉ cần được khởi tạo một lần,
khi đối tượng được tạo ra.
Do đó, không cần thiết phải tạo các phương thức riêng
để truy cập và thao tác với các thuộc tính này.
Việc chỉ có một phương thức cũng làm cho mã nguồn
của lớp Collatz trở nên gọn gàng và dễ hiểu hơn.
"""
class Collatz:
    def __init__(self, first_value):
        """Bắt đầu khởi tạo các thuộc tính bằng cách gán giá trị ban đầu"""
        self.chain = [first_value]
        self.length = 1
        self.max_value = first_value

        """tiếp tục tính toán các thuộc tính""" 
        n = first_value
        while n > 1:
            n = n // 2 if n % 2 == 0 else 3 * n + 1
            self.chain.append(n)
            self.length += 1
            if self.max_value < n: self.max_value = n
        """đã xong quá trình khởi tạo."""    

a = Collatz(84)
#print('Dãy Collatz: ', a.chain)
#print('Dãy Collatz: ', "->".join(str(i) for i in a.chain))
print('Dãy Collatz: ', "->".join(map(str, a.chain)))
print('Độ dài: ', a.length)
print('GTLN: ', a.max_value)