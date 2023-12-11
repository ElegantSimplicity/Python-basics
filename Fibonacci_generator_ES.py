# Sửa từ
# https://github.com/davecom/ClassicComputerScienceProblemsInPython/blob/master/Chapter1/fib6.py

def fib6(n):
    last = 0  
    next = 1  
    for _ in range(n):
        last, next = next, last + next
        yield next  # main generation step

if __name__ == "__main__":
    for i in fib6(100):
        print(i, end = ' ')