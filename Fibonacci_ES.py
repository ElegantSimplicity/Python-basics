# n-th Fibonacci
# https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
# không so sánh các cách thì chán chết!
import time

# Cách 1: dùng while
def fib(n):
    a, b = 1, 1
    k=2
    while k < n:
        a, b = b, a+b
        k +=1
    return b

# https://codereview.stackexchange.com/a/165060/237307
# Cách 1b: mã đẹp ES 
def fibb(n) :
    a, b = 1, 1
    while n > 2 :
        a, b, n = b, a+b, n-1
    return b

# Cách 1c: mã đẹp ES
def fibc(n):
    a, b, k = 1, 1, 2
    while k < n :
        a, b, k = b, a+b, k+1
    return b

#n=18
#for i in range(1,n):
 #  print(fib(i),fibb(i),fibc(i))

# Cách 2: dùng for
def fibo(n):
    a, b = 1, 1
    for i in range(3,n+1):
        a, b = b, a+b
    return b

###############################
# Cách 3: hồi qui tuy đẹp nhưng rất tốn time
def Fib(n):    # for n-th Fibonacci
    if n==1: return 1
    elif n==2: return 1
    else: return Fib(n-1)+Fib(n-2)


#print(Fib(50))          # n=50 đã tính mệt mỏi lắm rồi


##############################
# use the technique of memoization: cache = bộ nhớ đệm
# (xem Dynamic Programming)
# Tuy nhiên lại tốn bộ nhớ cho cache
# https://codereview.stackexchange.com/a/165004/237307

cache = {}          # bộ nhớ đệm
def fibonacci(n):
    if n in cache:
        return cache[n]

    if n==1: return 1
    elif n==2: return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        cache[n] = result
        return result

# So sánh thời gian
#n=20_000  # cách 1,2 vẫn dùng tốt, hết 1/100 s; cách cache lỗi so sánh
#n=1_000  # cách 1,2 vẫn dùng tốt; cách cache lỗi so sánh
n=960  # max
#n=50
start=time.time()
print(fib(n))
print("Done in ",time.time()-start)

start=time.time()
print(fibo(n))
print("Done in ",time.time()-start)

#start=time.time()
#print(fibonacci(n))     
#print("Done in ",time.time()-start)

start=time.time()
print('\nProbability of the digits:')

# Tò mò 1: tần xuất các chữ số có đều nhau không?
#s=''
#for i in range(1,n+1): s +=str(fib(i))
s="".join(str(fib(i)) for i in range(1,n+1))  # pythonic

for i in range(10):
    print(str(i)+' is ', s.count(str(i))/len(s))
print("Done in ",time.time()-start)

# Fact 2: The series of last digits repeats with a cycle length of 60 
# https://www.geeksforgeeks.org/interesting-facts-fibonacci-numbers/
#
for i in range(1, n - 1):
    # Since first two number are 0 and 1
    # so, if any two consecutive number encounter 0 and 1
    # at their unit place, then it clearly means that
    # number is repeating/ since we just have to find
    # the sum of previous two number
    if((fib(i) % 10 == 0) and (fib(i+1) % 10 == 1)):
            break
 
print("Sequence is repeating after index", i)   # 60
