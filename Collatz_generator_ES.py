def collatz(n):
    """Collatz sequence generator function"""
    yield n
    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        yield n

if __name__ == '__main__':
    n = 31
    print(type(collatz(n)))
    a = tuple(collatz(n))
    print(f"Collatz sequence for {n} (the length {len(a)} and the maximum {max(a)}) is: \n{a}")
    
    """ Cách viết khác:
    for n in range(2,2):
        for i in collatz(n):
            if i == 1:
                print(i)
            else:
                print(i, end = '->')
        print()    
    """