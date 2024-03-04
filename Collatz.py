# the Collatz function
# Example: n=13, length=9, chain: 13,40,20,10,5,16,8,4,2,1
# https://projecteuler.net/problem=14
# Nên tách riêng 2 hàm Collatz_length và Collatz_chain 

#Collatz = lambda n : n // 2 if n % 2 == 0 else 3 * n + 1

#from time import time

def Collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def Collatz_length(n):
    length = 1
    while n > 1:
        n = Collatz(n)
        length += 1
    return length

def Collatz_max_value(n):
    max_value = n
    while n > 1:
        n = Collatz(n)
        if max_value < n:
            max_value = n
    return max_value

def Collatz_chain(n):
    chain = [n]
    while n > 1:
        n = Collatz(n)
        chain.append(n)
    return chain

if __name__ == '__main__':
    n = 10**50
    for i in range(n,n+1):
        print(i, Collatz_length(i), Collatz_max_value(i), Collatz_chain(i)) 

    #n=1_000
    #start = time()
    #maxlength = max((Collatz_length(i) for i in range(2,n)))
    #print('Longest Collatz Sequence: ', maxlength)
    #print('Done in ',time()-start)