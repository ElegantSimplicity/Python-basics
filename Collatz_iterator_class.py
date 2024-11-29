class Collatz():
    """Collatz sequence iterator"""
    
    def __init__(self, start):
        self.number = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 1:
            raise StopIteration()
        if self.number % 2 == 0:
            self.number = self.number // 2
        else:
            self.number = 3 * self.number + 1
        return self.number
    
if __name__ == '__main__':
    n = 31
    a = tuple(Collatz(n))
    #print(type(Collatz(n)))
    print(f"Collatz sequence for {n} (the length {len(a)} and the maximum {max(a)}) is: \n{a}")
    
    #""" Cách viết khác:
    for n in range(29,32):
        for i in Collatz(n):
            if i == 1:
                print(i)
            else:
                print(i, end = '->')
        print()    
    #"""
