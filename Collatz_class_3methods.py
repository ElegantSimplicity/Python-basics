def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

class Collatz:
    def __init__(self, value):
        self.value = value

    def sequence(self):
        tmp_sequence = [self.value]
        current_value = self.value  # Tạo một bản sao của self.value
        while current_value > 1:
            current_value = collatz(current_value)
            tmp_sequence.append(current_value)
        return tmp_sequence

    def length(self):
        current_value = self.value  # Tạo một bản sao của self.value
        tmp_length = 1
        while current_value > 1:
            current_value = collatz(current_value)
            tmp_length += 1
        return tmp_length

    def max_value(self):
        current_value = self.value  # Tạo một bản sao của self.value
        max_value = self.value
        while current_value > 1:
            current_value = collatz(current_value)
            if current_value > max_value:
                max_value = current_value
        return max_value

a = Collatz(31)
print('Dãy Collatz: ', a.sequence())
print(' Độ dài: ',     a.length()) 
print(' GTLN: ',       a.max_value())
