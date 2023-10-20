#import sys
"""
default of int_max_str_digits in my computer is 4300
I now increase it to 50_000
"""
#sys.set_int_max_str_digits(4200)

def fibo(n):
    # a beautiful idea: number as string
    if n == 0: return '2'    # '2' for Lucas sequence
    elif n == 1: return '1'    
    else:
        a, b = '0', '1'
        for i in range(2, n + 1):
            a, b = b, str(int(a) + int(b))
        return b

# Amazing! I can get 50_000 - th Fibonacci
n=2000
# from 1 to n-th Fibo
string_all_Fibos = t = ''.join(fibo(i) for i in range(1,n+1))
print('t = ',t,' with ',len(t))
print('Probabilities of the digits of the whole Fibonacci sequence:')
for i in range(10):
    print(f'  {str(i)} is {t.count(str(i)) * 100 /len(t):>5.2f} %')

print('\nConjecture: for any initial conditions, (0,1)-Fibonacci or (2,1)-Lucas,')
print('the digits of the whole sequence x_{n+2}=x_{n+1}+x_n')
print('follows the uniform distribution!')

""" REFERENCE
[1] 2016 https://math.stackexchange.com/questions/1845099/is-the-fibonacci-constant-0-11235813213455-a-normal-number
[2] 2022 preprint, The Fibonacci Sequence is Normal Base 10
    https://arxiv.org/abs/2202.08986

"""
