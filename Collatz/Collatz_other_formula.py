def collatz(n):
    k = n % 2
    return k + (5*k+1)*n//2

n = 13
chain, length, max_value = [n], 1, n
while n > 1:
    n = collatz(n)
    chain.append(n)
    length += 1
    max_value = max(max_value, n)
print('Chain: ',chain)
print('Length: ',length)
print('Max value: ',max_value)