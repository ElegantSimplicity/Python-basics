# Collatz: my ES code
# cách viết hàm cho output vào tham số mặc định của hàm, khỏi khởi tạo giá trị
# bắt chước từ https://codegolf.stackexchange.com/a/238200/86575

def collatz(n, collatz_chain=[], collatz_length=0, collatz_max=0):
    while n > 1:
        collatz_chain.append(n)
        collatz_length +=1
        collatz_max = max(n, collatz_max)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    collatz_chain.append(1)
    yield collatz_chain, collatz_length, collatz_max

#K=13
#K=31
# 2021 https://link.springer.com/article/10.1007/s11227-020-03368-x
K = 2.2*10**11 # mình nhầm! con số phải lớn hơn rất nhiều
for i in collatz(K):
    print('Collatz chain:', i[0])
    print('Collatz length:', i[1])
    print('Collatz max value:', i[2])
    
# dùng string
def collatz_ES(n, collatz_string="", collatz_length=0, collatz_max=0):
    while n > 1:
        collatz_string += str(n) + "->"
        collatz_length +=1
        collatz_max = max(n, collatz_max)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    collatz_string += str(1)
    yield collatz_string, collatz_length, collatz_max

for i in collatz_ES(K):
    print('Collatz chain:', i[0])
    print('Collatz length:', i[1])
    print('Collatz max value:', i[2])
    