#import sys
"""
default of int_max_str_digits in my computer is 4300
I now increase it to 50_000
"""
#sys.set_int_max_str_digits(4200)

def fibo(n):
    # a beautiful idea: number as string
    if n == 1: return '1'
    elif n == 2: return '1'    # '2' for Lucas sequence
    else:
        a, b = '1', '1'
        for i in range(3, n + 1):
            a, b = b, str(int(a) + int(b))
        return b

# Amazing! I can get 50_000 - th Fibonacci
n=2000
# only n-th Fibo
s = fibo(n)
print('s = ',s,' with ',len(s))
print(f'Probabilities of the digits of the {n}-th Fibonacci sequence:')
for i in range(10):
    print(f'  {str(i)} is {s.count(str(i)) * 100 /len(s):>5.2f} %') 

# from 1 to n-th Fibo
t = ''.join(fibo(i) for i in range(1,n+1))
print('t = ',t,' with ',len(t))
print('Probabilities of the digits of the whole Fibonacci sequence:')
for i in range(10):
    print(f'  {str(i)} is {t.count(str(i)) * 100 /len(t):>5.2f} %')
print('\nConjecture: for any initial conditions (1,1) or (1,2)')
print('the digits of the whole sequence x_{n+2}=x_{n+1}+x_n')
print('follows the uniform distribution!')
